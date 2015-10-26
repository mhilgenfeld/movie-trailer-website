class Movie(object):
    """ Movie entity to contain basic information on a movie.
        Arguments:
        title: string - Name of the movie
        plot: string - brief synopsis of the movie
        trailerUrl: string - YouTube URL link to trailer
        posterImageUrl: string - URL link to poster image, or local path to image
        releaseDate: string - Year of movie release
        boxOfficeGross: string - Earnings at box office
        rating: string - Movie rating
        runtime: string - Running time of movie (ex. 100 Mins)
        *args: string[] - Actors in the movie
    """

    def __init__(self, title, plot, trailerUrl, posterImageUrl, releaseDate, boxOfficeGross, rating, runtime, *args):
        self.title = title
        self.plot = plot
        self.trailer_url = trailerUrl
        self.poster_image_url = posterImageUrl
        self.release_date = releaseDate
        self.box_office_gross = boxOfficeGross
        self.rating = rating
        self.run_time = runtime
        self.actors = list(args)


