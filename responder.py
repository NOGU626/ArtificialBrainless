from random import choice
import re

class Responder:
    """AIの応答を制御する思考エンジンの基底クラス。
    
    メソッド：
    responder(str) -- ユーザの入力strを受け取り、思考結果を返す
    
    プロパティ:
    name -- Responderオブジェクトの名前
    
    memo:
    *args: 複数の引数をタプルとして受け取る
    **kwargs: 複数のキーワード引数を辞書として受け取る
    """
    
    def __init__(self,name,dictionary):
        """文字列を受け取り、自身のnameに設定する。
        辞書dictionaryを受け取り、自身のdictionaryに保持する"""
        self._name = name
        self._dictionary = dictionary
        
    def response(self,*args):
        """文字列を受け取り、思考した結果を返す"""
        pass
    
    @property
    def name(self):
        """応答オブジェクトの名前"""
        return self._name

class WhatResponder(Responder):
    """AIの応答を制御する思考エンジンクラス
    入力に対して疑問形で聞き返す。"""
    def response(self,text):
        """文字列をtextを受け取り、'{text}ってなに？'という形式で返す。"""
        return '{}ってなに？'.format(text)
  
class RandomResponder(Responder):
    """AIの応答を制御する思考エンジンクラス。
    登録された文字列からランダムなものを返す。
    """
    
    def response(self,_):
        """ユーザーからの入力は受け取るが、使用せずにランダムな応答を返す。"""
        return choice(self._dictionary.random)

class PatternResponder(Responder):
    """AIの応答を制御する思考エンジンクラス。
    登録されたパターンに反応し、関連する応答を返す。
    """

    def response(self, text):
        """ユーザーの入力に合致するパターンがあれば、関連するフレーズを返す。"""
        for ptn in self._dictionary.pattern:
            matcher = re.search(ptn['pattern'], text)
            if matcher:
                chosen_response = choice(ptn['phrases'].split('|'))
                print(">>>>>{0}".format(chosen_response))
                return chosen_response.replace('%match%', matcher[0])
        return choice(self._dictionary.random)