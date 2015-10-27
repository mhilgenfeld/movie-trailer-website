import re


class Media(object):
    """Base Class for a media type, containing basic description properties.
        Arguments:
            title: string - Name of the movie
            plot: string - brief synopsis of the movie
            releaseDate: string - Year of movie release
            trailerUrl: string - YouTube URL link to trailer
            posterImageUrl: string - URL link to poster image, or local path
            runtime: string - Running time of movie (ex. 100 Mins)
    """

    # A single movie entry html template
    movie_tile_content = '''
            <div class="col-md-6 col-lg-4 {tile_type}-tile text-center"
                data-trailer-youtube-id="{trailer_youtube_id}"
                data-toggle="modal" data-target="#trailer">
                <img src="{poster_image_url}" width="220" height="342">
                <h2>{movie_title}
                <small> ({release_date})</small>
                <img src="info.png" id="tooltip_{count}" class="tt"></img>
                </h2>
            </div>
            '''

    # A media tooltip html content template
    movie_tooltip_content = '''
    <div id="movie_tooltip_{count}">
        <h5>Plot <small>{plot}</small></h5>
        <h5>Run Time <small>{run_time}</small></h5>
    </div>
    '''

    def __init__(self, title, plot, releaseDate,
                 trailerUrl, posterImageUrl,
                 runtime=None, *args):
        self.title = title
        self.plot = plot
        self.run_time = runtime
        self.release_date = releaseDate
        self.trailer_url = trailerUrl
        self.poster_image_url = posterImageUrl
        self.actors = list(args)

    # Returns the formatted HTML for the media tile.
    def get_content_html(self, count, type):
        trailer_youtube_id = Media.extract_youtube_id_from_url(self.trailer_url)  # noqa

        return Media.movie_tile_content.format(
                trailer_youtube_id=trailer_youtube_id,
                poster_image_url=self.poster_image_url,
                movie_title=self.title,
                release_date=self.release_date,
                count=count,
                tile_type=type)

    # Returns the formatted HTML for the tooltip popup.
    def get_tooltip_html(self, count):
        return Media.movie_tooltip_content.format(plot=self.plot,
                                                  run_time=self.run_time,
                                                  count=count)

    def create_movie_actors_content(self):
        """ Creates the html output of actors
        Arguments:
        actors -- list of strings
        """

        content = ''
        for actor in self.actors:
            content += '</br>' + actor
        return content

    @staticmethod
    def extract_youtube_id_from_url(url):
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',
                                                         url)
        return (youtube_id_match.group(0) if youtube_id_match else None)


class Movie(Media):
    """ Movie entity to contain basic information on a movie.
        Arguments:
        title: string - Name of the movie
        plot: string - brief synopsis of the movie
        trailerUrl: string - YouTube URL link to trailer
        posterImageUrl: string - URL link to poster image, or local path
        releaseDate: string - Year of movie release
        boxOfficeGross: string - Earnings at box office
        rating: string - Movie rating
        runtime: string - Running time of movie (ex. 100 Mins)
        *args: string[] - Actors in the movie
    """

    # A movies tooltip html content template
    movie_tooltip_content = '''
    <div id="movie_tooltip_{count}">
        <h5>Plot <small>{plot}</small></h5>
        <h5>Rating <small>{rating}</small></h5>
        <h5>Box Office <small>{box_office_gross}</small></h5>
        <h5>Run Time <small>{run_time}</small></h5>
        <h5>Cast <small>{actors}</small></h5>
    </div>
    '''

    def __init__(self, title, plot,
                 trailerUrl, posterImageUrl,
                 releaseDate, boxOfficeGross,
                 rating, runtime=None, *args):
        self.release_date = releaseDate
        self.box_office_gross = boxOfficeGross
        self.rating = rating
        super(Movie, self).__init__(title, plot, releaseDate,
                                    trailerUrl, posterImageUrl,
                                    runtime, *args)

    # Returns the formatted HTML for the tooltip popup. Override
    def get_tooltip_html(self, count):
        content = Movie.movie_tooltip_content.format(
                plot=self.plot,
                rating=self.rating,
                box_office_gross=self.box_office_gross,
                run_time=self.run_time,
                actors=Media.create_movie_actors_content(self),
                count=count)
        return content

    type_name = "movie"


class Series(Media):
    def __init__(self, title, plot, releaseDate,
                 trailerUrl, posterImageUrl,
                 seasons, episodes, *args):
        self.seasons = seasons
        self.episodes = episodes
        super(Series, self).__init__(title, plot,
                                     releaseDate, trailerUrl,
                                     posterImageUrl, *args)

    # A movies tooltip html content template
    movie_tooltip_content = '''
    <div id="movie_tooltip_{count}">
        <h5>Plot <small>{plot}</small></h5>
        <h5>Initial Release <small>{release_year}</small></h5>
        <h5>Seasons <small>{seasons}</small></h5>
        <h5>Episodes <small>{episodes}</small></h5>
        <h5>Cast <small>{actors}</small></h5>
    </div>
    '''

    type_name = "series"

    # Returns the formatted HTML for the tooltip popup. Override
    def get_tooltip_html(self, count):
        content = Series.movie_tooltip_content.format(
                plot=self.plot,
                release_year=self.release_date,
                seasons=self.seasons,
                episodes=self.episodes,
                actors=Media.create_movie_actors_content(self),
                count=count)
        return content
