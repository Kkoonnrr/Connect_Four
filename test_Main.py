import unittest
from Code.Main import FourInRow
from Code.WrongMoveError import WrongMoveError


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.four_in_row = FourInRow(0, 0, 0)

    def test_two_coins_when_two_drop(self):
    #given
        given_board = [[0 for i in range(7)] for i in range(6)]
    #when
        given_board[0][0] = 0
        given_board[1][0] = 1
        self.four_in_row.create_board()
        self.four_in_row.drop(0, 0, 0)
        self.four_in_row.drop(0, 1, 1)
    #then
        self.assertEqual(given_board, self.four_in_row.board)

    def test_win_vertical(self):
    #given
        self.four_in_row.create_board()
        self.four_in_row.drop(0, 0, 1)
        self.four_in_row.drop(1, 0, 1)
        self.four_in_row.drop(2, 0, 1)
    #when
        self.four_in_row.drop(3, 0, 1)
    #then
        self.assertTrue(self.four_in_row.winning_check(1))

    def test_win_horizontal(self):
    # given
        self.four_in_row.create_board()
        self.four_in_row.drop(0, 0, 1)
        self.four_in_row.drop(0, 1, 1)
        self.four_in_row.drop(0, 2, 1)
    # when
        self.four_in_row.drop(0, 3, 1)
    # then
        self.assertTrue(self.four_in_row.winning_check(1))
    def test_win_diagonal(self):
    # given
        self.four_in_row.create_board()
        self.four_in_row.drop(0, 0, 1)
        self.four_in_row.drop(1, 1, 1)
        self.four_in_row.drop(2, 2, 1)
    # when
        self.four_in_row.drop(3, 3, 1)
    # then
        self.assertTrue(self.four_in_row.winning_check(1))
    def test_is_board_full(self):
    #given
        self.four_in_row.board = [[2, 2, 2, 1, 2, 2, 2],
                           [1, 1, 1, 2, 1, 1, 1],
                           [2, 2, 2, 1, 2, 2, 2],
                           [1, 1, 1, 2, 1, 1, 1],
                           [2, 2, 2, 1, 2, 2, 2],
                           [1, 1, 1, 2, 1, 1, 1]]
    # when
        full = self.four_in_row.full_board()
    # then
        self.assertTrue(full)

    def test_win_when_longer_than_winning_score(self):
    # given
        self.four_in_row.create_board()
        self.four_in_row.drop(0, 0, 1)
        self.four_in_row.drop(1, 0, 1)
        self.four_in_row.drop(2, 0, 1)

        self.four_in_row.drop(4, 0, 1)
        self.four_in_row.drop(5, 0, 1)
        self.four_in_row.drop(6, 0, 1)
    # when
        self.four_in_row.drop(3, 0, 1)
    # then
        self.assertTrue(self.four_in_row.winning_check(1))

    def test_error_when_full_column(self):
    # given
        self.four_in_row.create_board()
        self.four_in_row.drop(0, 0, 1)
        self.four_in_row.drop(0, 1, 1)
        self.four_in_row.drop(0, 2, 1)
        self.four_in_row.drop(0, 3, 1)
        self.four_in_row.drop(0, 4, 1)
        self.four_in_row.drop(0, 5, 1)
    # when

    # then
        self.assertRaises(WrongMoveError, self.four_in_row.next_free_space, 0)


if __name__ == "__main__":
    unittest.main()
