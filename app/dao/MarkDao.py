from app.dao.GenericDao import GenericDao
from app.model.MarkModel import Mark


class MarkDao(GenericDao):
    def __init__(self):
        super().__init__()


    def place_mark(self, game_id, player_name, col_num, row_num):

        mark_to_update = self.db.session.query(Mark).filter(Mark.col_num == col_num). \
            filter(Mark.row_num == row_num). \
            filter(Mark.game_id == game_id).first()

        if mark_to_update.player_name is not None:
            return False

        self.db.session.query(Mark).filter(Mark.col_num == col_num). \
            filter(Mark.row_num == row_num). \
            filter(Mark.game_id == game_id). \
            update({"player_name": player_name})

        self.db.session.commit()

        return True

