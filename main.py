import streamlit as st

st.set_page_config(
    page_title="F1 2026 시즌 대시보드",
    page_icon="🏎️",
    layout="wide"
)

# Custom CSS - 상단 공백을 완전히 박멸하고 F1 로고 및 빨간 줄을 완전히 제거
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    .stApp {
        background: linear-gradient(135deg, #07090f 0%, #11151f 50%, #030406 100%);
        color: #ffffff !important;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* Streamlit 상단 기본 여백 완전 박멸 */
    header[data-testid="stHeader"] {
        background: transparent;
        display: none;
    }

    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        margin-top: -3rem !important;
    }

    /* 하얀 글씨 보장 */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #ffffff !important;
    }

    /* 팀 카드 디자인 */
    .team-card {
        background: rgba(18, 23, 33, 0.9);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
    }

    .team-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.6rem;
        font-weight: 900;
    }

    .stat-badge {
        display: inline-block;
        background: rgba(225, 6, 0, 0.25);
        border: 1px solid rgba(225, 6, 0, 0.6);
        color: #ff6b6b !important;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-right: 8px;
        margin-top: 8px;
    }

    /* 드라이버 심층 설명 박스 */
    .driver-detail-box {
        background: #111622;
        border-radius: 12px;
        border: 1px solid #e10600;
        padding: 22px;
        margin-top: 15px;
        box-shadow: 0 4px 20px rgba(225, 6, 0, 0.25);
    }
    </style>
""", unsafe_allow_html=True)

# 2026 시즌 전체 11개 팀 및 22명 선수 데이터베이스 (서사 포함)
f1_teams_database = [
    {
        "team_en": "Mercedes-AMG Petronas F1 Team", "team_kr": "메르세데스", "color": "#27F4D2", "principal": "Toto Wolff", "power_unit": "Mercedes",
        "drivers": [
            {"name_en": "Kimi Antonelli", "name_kr": "키미 안토넬리", "number": "12", "country": "이탈리아 🇮🇹", "birth": "2006.08.25", "story": "주니어 시절부터 압도적인 재능으로 '넥스트 베르스타펜'으로 지목받았습니다. 메르세데스 메인 시트에 데뷔하자마자 시즌 초반부터 경이로운 주행을 선보이며 수차례 우승을 거머쥔 2026시즌 최강의 영건입니다."},
            {"name_en": "George Russell", "name_kr": "조지 러셀", "number": "63", "country": "영국 🇬🇧", "birth": "1998.02.15", "story": "극단적인 예선 집중력과 타협 없는 주행을 보여주는 '미스터 토요일'입니다. 냉철한 판단력으로 은빛 화살 메르세데스의 황금기를 이끌고 있는 팀의 든든한 리더입니다."}
        ]
    },
    {
        "team_en": "Scuderia Ferrari", "team_kr": "페라리", "color": "#E8002d", "principal": "Frédéric Vasseur", "power_unit": "Ferrari",
        "drivers": [
            {"name_en": "Lewis Hamilton", "name_kr": "루이스 해밀턴", "number": "44", "country": "영국 🇬🇧", "birth": "1985.01.07", "story": "통산 7회 월드 챔피언에 빛나는 F1 역사상 가장 위대한 살아있는 전설입니다. 페라리로 이적하여 스칼렛 레드 머신을 타고 통산 8번째 월드 타이틀을 향해 목숨을 건 레이스를 펼치고 있습니다."},
            {"name_en": "Charles Leclerc", "name_kr": "샤를 르클레르", "number": "16", "country": "모나코 🇲🇨", "birth": "1997.10.16", "story": "페라리가 배출한 역대급 원랩 스페셜리스트이자 모나코의 영웅입니다
