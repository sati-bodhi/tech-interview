import unittest
import video_sourcing as vs


class TestSourcing(unittest.TestCase):

    def test_video_search(self):

        self.assertEqual(vs.video_search("Clock on the wall turning"),
                         "https://pexels.com/video/6339299/download")
