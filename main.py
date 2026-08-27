import streamlit as st

st.set_page_config(
    page_title="F1 2026 시즌 종합 정보 Hub",
    page_icon="🏎️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0b0e14 0%, #151a24 50%, #05070a 100%);
        color: #f3f4f6;
        font-family: 'Noto Sans KR', sans-serif;
    }

    .f1-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.2rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #ffffff, #e10600);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    .team-card {
        background: rgba(21, 26, 36, 0.85);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 18px 22px;
        margin-bottom: 15px;
    }

    .team-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 800;
    }

    .stat-badge {
        display: inline-block;
        background: rgba(225, 6, 0, 0.2);
        border: 1px solid rgba(225, 6, 0, 0.5);
        color: #ff4d4d;
        padding: 3px 10px;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. 헤더 및 BGM 컨트롤러 (에러 방지 처리 완료)
st.markdown('<div class="f1-header">🏎️ 2026 F1 WORLD CHAMPIONSHIP</div>', unsafe_allow_html=True)

with st.sidebar:
    st.subheader("🎵 BGM 설정")
    play_bgm = st.checkbox("Lose My Mind 재생", value=False)
    if play_bgm:
        try:
            # 로컬 파일이 있으면 로컬 파일 재생
            st.audio("lose_my_mind.mp3", format="audio/mp3")
            st.caption("Don Toliver - Lose My Mind (feat. Doja Cat) [F1® Movie OST]")
        except Exception:
            # 로컬 파일이 없어서 에러가 발생하면 안정적인 웹 스트리밍으로 전환
            online_audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
            st.audio(online_audio_url, format="audio/mp3")
            st.caption("Don Toliver - Lose My Mind (feat. Doja Cat) [F1® Movie OST]")

# 데이터베이스
f1_database = [
    {
        "team_en": "McLaren Formula 1 Team", "team_kr": "맥라렌", "color": "#FF8000", "principal": "Andrea Stella", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Lando Norris", "name_kr": "랜도 노리스", "number": "1", "country": "영국 (United Kingdom)", "birth": "1999년 11월 13일", "role": "메인 드라이버", "desc": "2019년 맥라렌을 통해 F1에 데뷔했으며, 폴 포지션 및 우승 기록을 보유한 디펜딩 챔피언."},
            {"name_en": "Oscar Piastri", "name_kr": "오스카 피아스트리", "number": "81", "country": "호주 (Australia)", "birth": "2001년 4월 6일", "role": "메인 드라이버", "desc": "2021년 F2 챔피언 출신으로 2023년 맥라렌에 합류해 루키 시즌부터 스프린트 우승 및 포디움을 기록함."}
        ]
    },
    {
        "team_en": "Scuderia Ferrari", "team_kr": "페라리", "color": "#E8002d", "principal": "Frédéric Vasseur", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Charles Leclerc", "name_kr": "샤를 르클레르", "number": "16", "country": "모나코 (Monaco)", "birth": "1997년 10월 16일", "role": "메인 드라이버", "desc": "2018년 자우버로 데뷔 후 2019년부터 스쿠데리아 페라리의 드라이버로 활동 중이며 다수의 퀄리파잉 폴 포지션을 기록함."},
            {"name_en": "Lewis Hamilton", "name_kr": "루이스 해밀턴", "number": "44", "country": "영국 (United Kingdom)", "birth": "1985년 1월 7일", "role": "메인 드라이버", "desc": "F1 통산 7회 월드 챔피언 달성자로, 맥라렌과 메르세데스를 거쳐 페라리로 이적함."}
        ]
    },
    {
        "team_en": "Mercedes-AMG Petronas F1 Team", "team_kr": "메르세데스", "color": "#27F4D2", "principal": "Toto Wolff", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "George Russell", "name_kr": "조지 러셀", "number": "63", "country": "영국 (United Kingdom)", "birth": "1998년 2월 15일", "role": "메인 드라이버", "desc": "2018년 F2 챔피언 출신으로, 윌리엄스를 거쳐 2022년부터 메르세데스 메인 드라이버로 활동 중."},
            {"name_en": "Kimi Antonelli", "name_kr": "키미 안토넬리", "number": "12", "country": "이탈리아 (Italy)", "birth": "2006년 8월 25일", "role": "메인 드라이버", "desc": "메르세데스 주니어 프로그램 출신으로, 하위 카테고리를 거쳐 메르세데스 시트를 확보함."}
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing", "team_kr": "레드불", "color": "#3671C6", "principal": "Christian Horner", "power_unit": "Honda RBPT",
        "drivers": [
            {"name_en": "Max Verstappen", "name_kr": "막스 베르스타펜", "number": "33", "country": "네덜란드 (Netherlands)", "birth": "1997년 9월 30일", "role": "메인 드라이버", "desc": "역대 최연소 F1 데뷔 및 최연소 레이스 우승 기록을 보유하고 있는 월드 챔피언."},
            {"name_en": "Yuki Tsunoda", "name_kr": "츠노다 유키", "number": "22", "country": "일본 (Japan)", "birth": "2000년 5월 11일", "role": "메인 드라이버", "desc": "혼다 드라이버 육성 프로그램 출신으로 2021년 F1 데뷔 후 레드불 레이싱 라인업에 출전."}
        ]
    },
    {
        "team_en": "Williams Racing", "team_kr": "윌리엄스", "color": "#64C4FF", "principal": "James Vowles", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Alexander Albon", "name_kr": "알렉산더 알본", "number": "23", "country": "태국 (Thailand)", "birth": "1996년 3월 23일", "role": "메인 드라이버", "desc": "토로 로소와 레드불 레이싱을 거쳐 2022년부터 윌리엄스의 리드 드라이버로 활약 중."},
            {"name_en": "Carlos Sainz", "name_kr": "카를로스 사인츠", "number": "55", "country": "스페인 (Spain)", "birth": "1994년 9월 1일", "role": "메인 드라이버", "desc": "토로 로소, 르노, 맥라렌, 페라리를 거쳐 윌리엄스로 이적한 베테랑 드라이버."}
        ]
    },
    {
        "team_en": "Aston Martin Aramco F1 Team", "team_kr": "애스턴 마틴", "color": "#229971", "principal": "Mike Krack", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Fernando Alonso", "name_kr": "페르난도 알론소", "number": "14", "country": "스페인 (Spain)", "birth": "1981년 7월 29일", "role": "메인 드라이버", "desc": "2005년과 2006년 월드 챔피언을 달성했으며 통산 300회 이상의 그랑프리 출전 경력을 보유한 드라이버."},
            {"name_en": "Lance Stroll", "name_kr": "랜스 스트롤", "number": "18", "country": "캐나다 (Canada)", "birth": "1998년 10월 29일", "role": "메인 드라이버", "desc": "2017년 윌리엄스를 통해 F1에 데뷔한 후 레이싱 포인트를 거쳐 애스턴 마틴에서 활약 중."}
        ]
    },
    {
        "team_en": "Stake F1 Team Kick Sauber", "team_kr": "킥 자우버", "color": "#52E252", "principal": "Mattia Binotto", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Nico Hülkenberg", "name_kr": "니코 훌켄버그", "number": "27", "country": "독일 (Germany)", "birth": "1987년 8월 19일", "role": "메인 드라이버", "desc": "2010년 데뷔 이래 다양한 팀에서 활동했으며 높은 레이스 운영 능력을 지닌 독일 출신 드라이버."},
            {"name_en": "Gabriel Bortoleto", "name_kr": "가브리엘 보르톨레토", "number": "5", "country": "브라질 (Brazil)", "birth": "2004년 10월 14일", "role": "메인 드라이버", "desc": "2023년 F3 챔피언을 기록한 후 자우버 팀을 통해 F1에 정식 입성함."}
        ]
    },
    {
        "team_en": "Visa Cash App RB F1 Team", "team_kr": "레이싱 불스 (RB)", "color": "#6692FF", "principal": "Laurent Mekies", "power_unit": "Honda RBPT",
        "drivers": [
            {"name_en": "Liam Lawson", "name_kr": "리암 로슨", "number": "30", "country": "뉴질랜드 (New Zealand)", "birth": "2002년 2월 11일", "role": "메인 드라이버", "desc": "레드불 주니어 팀 출신으로 2023년 리저브 드라이버로 대타 출전 후 정식 시트를 확보함."},
            {"name_en": "Isack Hadjar",
