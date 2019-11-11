# tictactoe_ai.py
# From Classic Computer Science Problems in Python Chapter 8
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from minimax import find_best_move
from connectfour import C4Board
from board import Move, Board

board: Board = C4Board()


def get_player_move() -> Move:
    player_move: Move = Move(-1)
    while player_move not in board.legal_moves:
        play: int = int(input("이동할 열 위치를 입력하세요 (0-6): "))
        player_move = Move(play)
    return player_move


if __name__ == "__main__":
    # 메인 게임 루프
    while True:
        human_move: Move = get_player_move()
        board = board.move(human_move)
        if board.is_win:
            print("당신이 이겼습니다!")
            break
        elif board.is_draw:
            print("비겼습니다!")
            break
        computer_move: Move = find_best_move(board, 5)
        print(f"컴퓨터가 {computer_move}열을 선택했습니다.")
        board = board.move(computer_move)
        print(board)
        if board.is_win:
            print("컴퓨터가 이겼습니다!")
            break
        elif board.is_draw:
            print("비겼습니다!")
            break
