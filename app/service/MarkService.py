from app.dao.MarkDao import MarkDao


class MarkService:

    def __init__(self):
        self.mark_dao = MarkDao()

    def place_mark(self, game_id, player_name, col_num, row_num):

        return self.mark_dao.place_mark(game_id, player_name, col_num, row_num)



