# vocabtra
Japanese-Kanji Vocabulary Extraction Application
python -m venv myenv 
source myenv/bin/activate   

curl  -X POST http://localhost:8000/extractors/ -u admin:admin -H "Content-Type: application/json" -d '{"content": "【エルサレム＝福島利之、ワシント ン＝田島大志】イスラム主義組織ハマスによる７日のイスラエルへの奇襲攻撃を巡り、イスラエルと米国によるインテリジェンス（情報収集・分析）上の失態だったとの指摘が出ている。両国とも世界最高水準の情報機関を擁しながらハマスの攻撃を十分に事前察知できず、多くの犠牲者を出したことになる。"}'
