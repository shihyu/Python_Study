srt.py 程式碼來自[http://github.com/riobard/srt.py/blob/724a5941fc0040d7265e05ed0296bb2622f2d1d6/srt.py#]

使用
python srt.py split subtitle.srt 42:30 45:10
切割長度 45:10，再切割長度 42:30 如果還有剩下則在分割成一個

長度43分鐘，每10分鐘切一段可用
python srt.py split subtitle.srt 10:00 10:0 10:00 10:00

python srt.py shift subtitle.srt -,500 > new.subtitle.srt
字幕時間向前偏移 50ms，並輸出成 new.subtitle.srt

