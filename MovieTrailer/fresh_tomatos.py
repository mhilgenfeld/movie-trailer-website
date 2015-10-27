import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <script src="http://code.jquery.com/jquery-1.10.1.min.js">
        </script>
    <link rel="stylesheet"
        href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet"
        href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <link rel="stylesheet"
        href="http://cdn.jsdelivr.net/qtip2/2.2.1/jquery.qtip.min.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js">
        </script>
    <script src="http://cdn.jsdelivr.net/qtip2/2.2.1/jquery.qtip.min.js">
        </script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 15px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .series-tile {
            margin-bottom: 20px;
            padding-top: 15px;
        }
        .series-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .tt{
            height: 25px;
            width: 25px;
        }

    </style>
    <script type="text/javascript" charset="utf-8">
         $(document).ready(function() {
            $('.tt[id^="tooltip_"]').each(function(){
                $(this).qtip({
                    content: $('#movie_' + $(this).attr('id')),
                        show: {
                        delay:250
                    },
                    hide: {
                        fixed: true,
                        delay: 180
                    },
                    style: {
                        classes: 'qtip-dark qtip-shadow',
                    },
                    position: {
                        my: 'bottom center',
                        at: 'top center'
                    }
                });
            });
        });

        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close,
                      .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed,
            // as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl =
            'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty()
                                         .append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        $(document).on('click', '.series-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl =
            'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty()
                                         .append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first()
                                 .show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>

  <div style="display: none;">
    {tooltips}
  </div>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#"
             class="hanging-close"
             data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container-fluid">
              <div class="navbar-header">

                <a class="navbar-brand" href="#movies">Fresh Tomatoes</a>
              </div>
              <div class="collapse navbar-collapse">
                <ul id="tabs" class="nav navbar-nav" data-tabs="tabs">
                    <li class="active">
                        <a href="#movies" data-toggle="tab">Movies</a></li>
                    <li><a href="#series" data-toggle="tab">TV Series</a></li>
                </ul>
            </div>
        </div>
      </div>
    </div>
    <div class="tab-content">
        <div id="movies" class="tab-pane active">
            {movie_tiles}
        </div>
        <div id="series" class="tab-pane ">
            {series_tiles}
        </div>
    </div>
  </body>
</html>
'''


def create_movie_tiles_content(movies, counter=0):
    """ Creates the html output for each of the Movie's content.
    Arguments:
    movies -- list of media.Movie
    Returns string of formatted html
    """
    count = counter if counter > 0 else 0
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in,
        # and add count for popup css
        content += movie.get_content_html(count, movie.type_name)
        count = count + 1
    return content


def create_movie_tooltip_content(movies, series):
    """ Creates the html output for each of the Movie's tooltip popup.
    Arguments:
    movies -- list of media.Movie
    Returns string of formatted html
    """
    # The HTML content for the movie tooltip popup
    count = 0
    content = ''
    for movie in movies:
        content += movie.get_tooltip_html(count)
        count = count + 1

    for s in series:
        content += s.get_tooltip_html(count)
        count = count + 1

    return content


def open_movies_page(movies, series):
    """ Builds the html content for webpage, creates the html file,
        and opens a browser to that file.
        Arguments:
        movies -- list of media.Movie
    """
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
            tooltips=create_movie_tooltip_content(movies, series),
            movie_tiles=create_movie_tiles_content(movies),
            series_tiles=create_movie_tiles_content(series, len(movies)))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
