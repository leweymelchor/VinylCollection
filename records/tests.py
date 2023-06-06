from django.test import TestCase

# Create your tests here.
from records.models import Artist, Record


class ArtistTestCase(TestCase):
    def testPost(self):
        artist = Artist(artist="Megadeth")
        self.assertEqual(artist.artist, "Megadeth")


# class RecordTestCase(TestCase):
#     def testPost(self):
#         record = Record(album="Rust In Piece", artist="Megadeth", artwork="https://upload.wikimedia.org/wikipedia/en/d/dc/Megadeth-RustInPeace.jpg", date="1990-09-24", price="39.99", owner="Lewey")
#         self.assertEqual(record.album, "Rust In Piece")
#         self.assertEqual(record.records, "Megadeth")
#         self.assertEqual(record.artwork, "https://upload.wikimedia.org/wikipedia/en/d/dc/Megadeth-RustInPeace.jpg")
#         self.assertEqual(record.date, "1990-09-24")
#         self.assertEqual(record.price, "39.99")
#         self.assertEqual(record.owner, "Lewey")
