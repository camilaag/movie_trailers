import media
import fresh_tomatoes

""" Essa classe seta as informacoes dos filmes criando instancias da classe media """

scream = media.Movie('Scream','A year after the murder of her mother, a teenage girl is terrorized by a new killer, who targets the girl and her friends by using horror films as part of a deadly game.',
                        'https://upload.wikimedia.org/wikipedia/pt/5/5f/Scream_p%C3%B4ster.jpg',
                        'https://www.youtube.com/watch?v=AWm_mkbdpCA')

her = media.Movie('Her','In a near future, a lonely writer develops an unlikely relationship with an operating system designed to meet his every need.',
                        'https://m.media-amazon.com/images/M/MV5BMjA1Nzk0OTM2OF5BMl5BanBnXkFtZTgwNjU2NjEwMDE@._V1_.jpg',
                        'https://www.youtube.com/watch?v=ne6p6MfLBxc')

coco = media.Movie('Coco',"Aspiring musician Miguel, confronted with his family's ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.",
                        'https://m.media-amazon.com/images/M/MV5BYjQ5NjM0Y2YtNjZkNC00ZDhkLWJjMWItN2QyNzFkMDE3ZjAxXkEyXkFqcGdeQXVyODIxMzk5NjA@._V1_SY1000_CR0,0,699,1000_AL_.jpg',
                        'https://www.youtube.com/watch?v=Rvr68u6k5sI')

fatal_attraction = media.Movie('Fatal Attraction',"A married man's one-night stand comes back to haunt him when that lover begins to stalk him and his family",
                        'https://m.media-amazon.com/images/M/MV5BYjBjNzNiNWYtYWU0NC00OTdjLTk3NmYtM2NjZjc2ZGIwOTQ1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg',
                        'https://www.youtube.com/watch?v=e3oF8Po4qWc')

shining = media.Movie('The shining','A family heads to an isolated hotel for the winter where an evil spiritual presence influences the father into violence, while his psychic son sees horrific forebodings from the past and of the future.',
                        'https://m.media-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg',
                        'https://www.youtube.com/watch?v=S014oGZiSdI')

american_beauty = media.Movie('American Beauty',"A sexually frustrated suburban father has a mid-life crisis after becoming infatuated with his daughter's best friend.",
                        'https://m.media-amazon.com/images/M/MV5BNTBmZWJkNjctNDhiNC00MGE2LWEwOTctZTk5OGVhMWMyNmVhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg',
                        'https://www.youtube.com/watch?v=3ycmmJ6rxA8')



movies = [scream,her,coco,fatal_attraction,shining,american_beauty]
fresh_tomatoes.open_movies_page(movies)
