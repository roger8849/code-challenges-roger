package co.edu.roger.algorithms;

import com.sap.security.core.server.csi.XSSEncoder;
import com.sap.acme.facades.wishlist.WishlistFacade;
import com.sap.sopra.miglog.facades.wishlist.data.WishlistData;
import com.sap.sopra.miglog.facades.wishlsit.data.WishlistEntryData;
import de.hybris.platform.acceleratorstorefrontcommons.controllers.pages.AbstractSearchPageController;
import de.hybris.platform.cms2.exceptions.CMSItemNotFoundException;
import de.hybris.platform.commercefacades.order.CartFacade;
import de.hybris.platform.commercefacades.product.data.ProductData;
import de.hybris.platform.commercefacades.search.ProductSearchFacade;
import de.hybris.platform.commercefacades.search.data.SearchQueryData;
import de.hybris.platform.commercefacades.search.data.SearchStateData;
import de.hybris.platform.commerceservices.search.facetdata.FacetData;
import de.hybris.platform.commerceservices.search.facetdata.FacetRefinement;
import de.hybris.platform.commerceservices.search.facetdata.FacetValueData;
import de.hybris.platform.commerceservices.search.facetdata.ProductSearchPageData;
import de.hybris.platform.commerceservices.search.pagedata.PageableData;
import de.hybris.platform.core.model.user.CustomerModel;
import de.hybris.platform.servicelayer.user.UserService;
import org.apache.commons.collections.CollectionUtils;
import org.apache.commons.lang.StringUtils;
import org.apache.log4j.Logger;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.annotation.Resource;
import java.io.UnsupportedEncodingException;
import java.math.BigDecimal;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

@Controller
@RequestMapping("/search")
public class SearchPageController extends AbstractSearchPageController {

    private static final Logger LOG = Logger.getLogger(SearchPageController.class);

    private static final String FACET_SEPARATOR = ":";

    @Resource(name = "productSearchFacade")
    private ProductSearchFacade<ProductData> productSearchFacade;

    @Resource(name = "cartFacade")
    private CartFacade cartFacade;

    @Resource(name = "wishlistFacade")
    private WishlistFacade wishlistFacade;

    @Resource(name = "userService")
    private UserService userService;

    private CustomerModel customer;

    private SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMdd");

    @ResponseBody
    @RequestMapping(value = "/results", method = RequestMethod.GET)
    public SearchResultsData<ProductData> jsonSearchResults(@RequestParam("q") final String searchQuery,
                                                            @RequestParam(value = "page", defaultValue = "0") final int page,
                                                            @RequestParam(value = "show", defaultValue = "Page") final ShowMode showMode,
                                                            @RequestParam(value = "sort", required = false) final String sortCode) throws CMSItemNotFoundException
    {
        final ProductSearchPageData<SearchStateData, ProductData> searchPageData = performSearch(searchQuery, page, showMode,
                sortCode, getSearchPageSize());
        final SearchResultsData<ProductData> searchResultsData = new SearchResultsData<>();
        searchResultsData.setResults(searchPageData.getResults());
        searchResultsData.setPagination(searchPageData.getPagination());
        return searchResultsData;
    }

    @ResponseBody
    @RequestMapping(value = "/facets", method = RequestMethod.GET)
    public FacetRefinement<SearchStateData> getFacets(@RequestParam("q") final String searchQuery,
                                                      @RequestParam(value = "page", defaultValue = "0") final int page,
                                                      @RequestParam(value = "show", defaultValue = "Page") final ShowMode showMode,
                                                      @RequestParam(value = "sort", required = false) final String sortCode) throws CMSItemNotFoundException
    {
        final SearchStateData searchState = new SearchStateData();
        final SearchQueryData searchQueryData = new SearchQueryData();
        searchQueryData.setValue(searchQuery);
        searchState.setQuery(searchQueryData);

        final ProductSearchPageData<SearchStateData, ProductData> searchPageData = productSearchFacade.textSearch(searchState,
                createPageableData(page, getSearchPageSize(), sortCode, showMode));
        final List<FacetData<SearchStateData>> facets = refineFacets(searchPageData.getFacets(),
                convertBreadcrumbsToFacets(searchPageData.getBreadcrumbs()));
        final FacetRefinement<SearchStateData> refinement = new FacetRefinement<>();
        refinement.setFacets(facets);
        refinement.setCount(searchPageData.getPagination().getTotalNumberOfResults());
        refinement.setBreadcrumbs(searchPageData.getBreadcrumbs());
        return refinement;
    }

    protected ProductSearchPageData<SearchStateData, ProductData> performSearch(final String searchQuery, final int page,
                                                                                final ShowMode showMode, final String sortCode, final int pageSize)
    {

        final PageableData pageableData = createPageableData(page, pageSize, sortCode, showMode);

        final SearchStateData searchState = new SearchStateData();
        final SearchQueryData searchQueryData = new SearchQueryData();
        searchQueryData.setValue(searchQuery);
        searchState.setQuery(searchQueryData);

        final ProductSearchPageData<SearchStateData, ProductData> searchPageData = productSearchFacade.textSearch(searchState, pageableData);

        postProcessSearchPageData(searchPageData);

        return encodeSearchPageData(searchPageData);

    }

    /**
     * post-process results of solr search
     * @param searchPageData
     */
    private void postProcessSearchPageData(final ProductSearchPageData<SearchStateData, ProductData> searchPageData) {

        // search results
        final List<ProductData> results = searchPageData.getResults();

        // search results are customized for the current user
        customer = (CustomerModel)userService.getCurrentUser();

        // users whishlist, this might return a long list of items
        final WishlistData wishlist = wishlistFacade.getUserWishlist(customer);

        // mark favourite products
        for (WishlistEntryData wishlistEntry : wishlist.getEntries()) {
            for (ProductData productData : results) {
                if (productData.getCode().equals(wishlistEntry.getProduct().getProductCode())) {
                    productData.setFavorite(Boolean.TRUE);
                }
            }
        }

        LOG.debug("user: " + this.customer + " cart code: " + cartFacade.getSessionCart().getCode());

        // increase price of  adults only products fby 20% for users younger than 18
        if (!isAdult()) {
            results.stream().filter(it -> it.getAdultsOnly()).forEach(it -> it.getPrice().setValue(it.getPrice().getValue().multiply(new BigDecimal(1.2))));
        }

    }

    /**
     * check customer is older than 18
     */
    private boolean isAdult() {

        int d1 = Integer.parseInt(sdf.format(customer.getDateOfBirth()));
        int d2 = Integer.parseInt(sdf.format(new Date()));
        int age = (d2 - d1) / 10000;
        return age >= 18;

    }

    protected ProductSearchPageData<SearchStateData, ProductData> encodeSearchPageData(
            final ProductSearchPageData<SearchStateData, ProductData> searchPageData) {

        final SearchStateData currentQuery = searchPageData.getCurrentQuery();

        if (currentQuery != null)
        {
            try
            {
                final SearchQueryData query = currentQuery.getQuery();
                final String encodedQueryValue = XSSEncoder.encodeHTML(query.getValue());
                query.setValue(encodedQueryValue);
                currentQuery.setQuery(query);
                searchPageData.setCurrentQuery(currentQuery);
                searchPageData.setFreeTextSearch(XSSEncoder.encodeHTML(searchPageData.getFreeTextSearch()));

                final List<FacetData<SearchStateData>> facets = searchPageData.getFacets();
                if (CollectionUtils.isNotEmpty(facets))
                {
                    processFacetData(facets);
                }
            }
            catch (final UnsupportedEncodingException e)
            {
                if (LOG.isDebugEnabled())
                {
                    LOG.debug("Error occured during Encoding the Search Page data values", e);
                }
            }
        }
        return searchPageData;
    }

    protected void processFacetData(final List<FacetData<SearchStateData>> facets) throws UnsupportedEncodingException
    {
        for (final FacetData<SearchStateData> facetData : facets)
        {
            final List<FacetValueData<SearchStateData>> topFacetValueDatas = facetData.getTopValues();
            if (CollectionUtils.isNotEmpty(topFacetValueDatas))
            {
                processFacetDatas(topFacetValueDatas);
            }
            final List<FacetValueData<SearchStateData>> facetValueDatas = facetData.getValues();
            if (CollectionUtils.isNotEmpty(facetValueDatas))
            {
                processFacetDatas(facetValueDatas);
            }
        }
    }

    protected void processFacetDatas(final List<FacetValueData<SearchStateData>> facetValueDatas)
            throws UnsupportedEncodingException
    {
        for (final FacetValueData<SearchStateData> facetValueData : facetValueDatas)
        {
            final SearchStateData facetQuery = facetValueData.getQuery();
            final SearchQueryData queryData = facetQuery.getQuery();
            final String queryValue = queryData.getValue();
            if (StringUtils.isNotBlank(queryValue))
            {
                final String[] queryValues = queryValue.split(FACET_SEPARATOR);
                final StringBuilder queryValueBuilder = new StringBuilder();
                queryValueBuilder.append(XSSEncoder.encodeHTML(queryValues[0]));
                for (int i = 1; i < queryValues.length; i++)
                {
                    queryValueBuilder.append(FACET_SEPARATOR).append(queryValues[i]);
                }
                queryData.setValue(queryValueBuilder.toString());
            }
        }
    }

}
