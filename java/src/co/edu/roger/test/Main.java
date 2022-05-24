package co.edu.roger.test;

public class Main {

    DVD[] dvdCollection = new DVD[15];

    public static void main(String[] args) {
        System.out.println("Hello World!");
    }

    // A simple definition for a DVD.
    public class DVD {
        public String name;
        public int releaseYear;
        public String director;

        public DVD(String name, int releaseYear, String director) {
            this.name = name;
            this.releaseYear = releaseYear;
            this.director = director;
        }

        public String toString() {
            return this.name + ", directed by " + this.director + ", released in " + this.releaseYear;
        }
    }
}

