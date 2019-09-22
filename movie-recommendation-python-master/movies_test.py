from StringIO import StringIO
import unittest
from movies import coerce_date, _ratings_iterator, _parse_movies
class MoviesTests(unittest.TestCase):

    def test_coerce_date(self):
        t = coerce_date(' 01-Nov-1995 ')
        self.assertEqual(t.tm_year, 1995)
        self.assertEqual(t.tm_mon, 11)
        self.assertEqual(t.tm_mday, 1)
        
        t = coerce_date('')
        self.assertIsNone(t)

    def test_parse_movies(self):
        movies_file = """
1|Toy Story (1995)|01-Jan-1995||http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)|0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0
14|Movie Without Release Date| ||http://us.imdb.com/M/title-exact?Postino,%20Il%20(1994)|0|0|0|0|0|0|0|0|1|0|0|0|0|0|1|0|0|0|0
        """
        movies = _parse_movies(StringIO(movies_file))
        self.assertTrue(1 in movies)
        self.assertTrue(14 in movies)
        toystory = movies[1]
        no_release_date = movies[14]
        
        self.assertEquals(toystory['name'], 'Toy Story (1995)')
        self.assertEquals(toystory['release_date'].tm_year, 1995)
        self.assertEquals(toystory['imdb_url'], 'http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)')
        toystory_genres = ['Animation', 'Children', 'Comedy']
        for g in toystory_genres:
            self.assertTrue(g in toystory['genres'])
        
        self.assertEquals('Movie Without Release Date', no_release_date['name'])
        self.assertIsNone(no_release_date['release_date'])
        
    def test_ratings_iterator(self):
        ratings_file = """
        196	242	3	881250949
186	302	3	891717742
22	377	1	878887116
244	51	2	880606923
166	346	1	886397596
        """
        
        ratings = tuple(_ratings_iterator(StringIO(ratings_file)))
        self.assertEqual(ratings[1].userid, 186)
        self.assertEqual(ratings[1].movieid, 302)
        self.assertEqual(ratings[1].rating, 3)
        self.assertEqual(ratings[1].timestamp, 891717742)
        
        self.assertEqual(ratings[3].userid, 244)
        self.assertEqual(ratings[3].movieid, 51)
        self.assertEqual(ratings[3].rating, 2)
        self.assertEqual(ratings[3].timestamp, 880606923)
        
if __name__ == '__main__':
    unittest.main()
