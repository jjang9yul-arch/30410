from datetime import datetime
import pandas as pd
import streamlit as st

# 페이지 설정을 가장 먼저 호출
st.set_page_config(
    page_title="F1 2026 World Championship",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for UI Enhancement
st.markdown(
    """
    <style>
    .main-header {
        text-align: center;
        padding: 10px;
    }
    .f1-logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 280px;
    }
    .card {
        background-color: #1e1e24;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        border-left: 5px solid #e10600;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .status-done {
        color: #4CAF50;
        font-weight: bold;
    }
    .status-upcoming {
        color: #FF9800;
        font-weight: bold;
    }
    .driver-badge {
        background-color: #2b2b36;
        padding: 10px 15px;
        border-radius: 8px;
        margin: 5px 0;
        border-left: 3px solid #e10600;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# F1 Header Logo
# ---------------------------------------------------------
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg", width=300
)
st.markdown(
    "<h1 style='text-align: center;'>2026 FORMULA 1 WORLD CHAMPIONSHIP</h1>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)
st.divider()

# ---------------------------------------------------------
# Data Definition
# ---------------------------------------------------------
teams_data = {
    "Red Bull Racing": {
        "engine": "Red Bull Ford Powertrains",
        "base": "Milton Keynes, United Kingdom",
        "description": "새로운 엔진 규정에 맞추어 포드(Ford)와 손잡고 파워유닛을 직접 개발한 레드불 레이싱입니다. 규정 변화 속에서도 최정상의 자리를 지키기 위해 도전하고 있습니다.",
        "drivers": [
            {
                "name": "막스 베르스타펜 (Max Verstappen)",
                "number": "3",
                "nationality": "네덜란드",
                "desc": "강력한 경기 운영 능력과 완벽한 레이스 페이스를 자랑하는 F1 월드 챔피언입니다.",
            },
            {
                "name": "아이작 하자르 (Isack Hadjar)",
                "number": "6",
                "nationality": "프랑스",
                "desc": "레드불 주니어 프로그램을 통해 선발된 공격적이고 과감한 드라이빙 스타일의 루키입니다.",
            },
        ],
    },
    "Ferrari": {
        "engine": "Ferrari",
        "base": "Maranello, Italy",
        "description": "F1 역사상 가장 성공적이고 오래된 역사적인 팀입니다. 강력한 자체 파워유닛과 명문팀으로서의 자부심을 바탕으로 챔피언십에 도전합니다.",
        "drivers": [
            {
                "name": "샤를 르클레르 (Charles Leclerc)",
                "number": "16",
                "nationality": "모나코",
                "desc": "압도적인 퀄리파잉 스피드를 자랑하는 페라리의 핵심 드라이버입니다.",
            },
            {
                "name": "루이스 해밀턴 (Lewis Hamilton)",
                "number": "44",
                "nationality": "영국",
                "desc": "7회 월드 챔피언이라는 풍부한 경험과 통산 최다 승 기록을 보유한 전설적인 드라이버입니다.",
            },
        ],
    },
    "Mercedes": {
        "engine": "Mercedes",
        "base": "Brackley, United Kingdom",
        "description": "터보 하이브리드 시대를 지배했던 막강한 파워유닛 기술력을 바탕으로 2026년 규정 변화를 통해 다시 정상 복귀를 노리는 은빛 화살 팀입니다.",
        "drivers": [
            {
                "name": "조지 러셀 (George Russell)",
                "number": "63",
                "nationality": "영국",
                "desc": "정교한 피드백과 꾸준한 성적으로 메르세데스를 이끌고 있는 리더 드라이버입니다.",
            },
            {
                "name": "키미 안토넬리 (Kimi Antonelli)",
                "number": "12",
                "nationality": "이탈리아",
                "desc": "엄청난 천재성과 잠재력으로 기대를 모으고 있는 차세대 super-rookie 드라이버입니다.",
            },
        ],
    },
    "McLaren": {
        "engine": "Mercedes",
        "base": "Woking, United Kingdom",
        "description": "뛰어난 섀시 개발 능력과 안정적인 팀 조직력을 통해 최근 몇 시즌 동안 가장 가파른 상승세를 보여준 전통의 명문 팀입니다.",
        "drivers": [
            {
                "name": "랜도 노리스 (Lando Norris)",
                "number": "1",
                "nationality": "영국",
                "desc": "맥라렌의 에이스로서 뛰어난 레이스 페이스와 안정감을 보여주는 드라이버입니다.",
            },
            {
                "name": "오스카 피아스트리 (Oscar Piastri)",
                "number": "81",
                "nationality": "호주",
                "desc": "침착함과 과감함을 겸비하여 데뷔 직후부터 최고 수준의 레이스를 보여준 드라이버입니다.",
            },
        ],
    },
    "Aston Martin": {
        "engine": "Honda",
        "base": "Silverstone, United Kingdom",
        "description": "2026년부터 혼다(Honda)와의 워크스 파트너십을 체결하여 독자적인 패키지를 구축하고 정상권을 위협하는 최첨단 시설의 팀입니다.",
        "drivers": [
            {
                "name": "페르난도 알론소 (Fernando Alonso)",
                "number": "14",
                "nationality": "스페인",
                "desc": "노련함과 대담한 경기 운영 능력을 갖춘 2회 월드 챔피언 베테랑 드라이버입니다.",
            },
            {
                "name": "랜스 스트롤 (Lance Stroll)",
                "number": "18",
                "nationality": "캐나다",
                "desc": "변화무쌍한 웨트 레이스 등 난조건에서 강점을 드러내는 드라이버입니다.",
            },
        ],
    },
    "Alpine": {
        "engine": "Mercedes",
        "base": "Enstone, United Kingdom",
        "description": "프랑스 르노 그룹 계열의 스포츠카 브랜드 알핀 팀입니다. 2026년부터 메르세데스 파워유닛을 탑재하여 재도약을 노립니다.",
        "drivers": [
            {
                "name": "피에르 개슬리 (Pierre Gasly)",
                "number": "10",
                "nationality": "프랑스",
                "desc": "그랑프리 우승 경험을 보유하고 있으며 정교한 드라이빙으로 상위권을 노립니다.",
            },
            {
                "name": "프랑코 콜라핀토 (Franco Colapinto)",
                "number": "43",
                "nationality": "아르헨티나",
                "desc": "남미 출신의 신예로 강렬한 스피드와 패기 있는 드라이빙을 선보입니다.",
            },
        ],
    },
    "Williams": {
        "engine": "Mercedes",
        "base": "Grove, United Kingdom",
        "description": "F1 역사의 한 축을 담당한 명문 윌리엄스입니다. 지속적인 리빌딩 과정을 거쳐 중위권 핵심으로 진입하고 있습니다.",
        "drivers": [
            {
                "name": "알렉산더 알본 (Alex Albon)",
                "number": "23",
                "nationality": "태국",
                "desc": "윌리엄스의 리빌딩을 주도해 온 확실한 기량과 리더십을 갖춘 드라이버입니다.",
            },
            {
                "name": "카를로스 사인츠 (Carlos Sainz)",
                "number": "55",
                "nationality": "스페인",
                "desc": "전략적인 두뇌와 안정성을 갖춘 그랑프리 우승자 출신 베테랑입니다.",
            },
        ],
    },
    "Racing Bulls": {
        "engine": "Red Bull Ford Powertrains",
        "base": "Faenza, Italy",
        "description": "레드불의 시스터 팀으로 젊고 유망한 신예들을 적극 기용하여 빠른 성장을 지향하는 이탈리아 기반의 팀입니다.",
        "drivers": [
            {
                "name": "리암 로슨 (Liam Lawson)",
                "number": "30",
                "nationality": "뉴질랜드",
                "desc": "여러 레이스에서 인상적인 추월 능력을 보여준 공격적인 스타일의 드라이버입니다.",
            },
            {
                "name": "아르비드 린드블라드 (Arvid Lindblad)",
                "number": "41",
                "nationality": "영국",
                "desc": "유스 카트 시절부터 압도적인 성과를 내며 F1에 진입한 대형 유망주입니다.",
            },
        ],
    },
    "Haas F1 Team": {
        "engine": "Ferrari",
        "base": "Kannapolis, United States",
        "description": "미국 자본 기반의 F1 팀으로 페라리와의 견고한 파트너십 및 도요타(TGR)의 기술 지원을 바탕으로 효율적이고 가성비 높은 레이싱을 선보입니다.",
        "drivers": [
            {
                "name": "에스테반 오콘 (Esteban Ocon)",
                "number": "31",
                "nationality": "프랑스",
                "desc": "단단한 수비력과 추월 기회를 놓치지 않는 결단력을 가진 드라이버입니다.",
            },
            {
                "name": "올리버 베어먼 (Oliver Bearman)",
                "number": "87",
                "nationality": "영국",
                "desc": "젊은 패기와 압도적인 페이스로 빠르게 스포트라이트를 받은 드라이버입니다.",
            },
        ],
    },
    "Audi": {
        "engine": "Audi",
        "base": "Hinwil, Switzerland",
        "description": "자우버(Sauber) 팀을 인수하여 2026년 파워유닛 및 워크스 팀으로 새롭게 F1에 정식 출사표를 던진 독일의 거대 모터스포츠 가문 아우디입니다.",
        "drivers": [
            {
                "name": "니코 휠켄베르크 (Nico Hülkenberg)",
                "number": "27",
                "nationality": "독일",
                "desc": "아우디 프로젝트의 개발을 끌어나갈 풍부한 경험을 갖춘 베테랑 드라이버입니다.",
            },
            {
                "name": "가브리에우 보르툴레투 (Gabriel Bortoleto)",
                "number": "5",
                "nationality": "브라질",
                "desc": "하위 카테고리 챔피언 출신으로 아우디의 미래를 담당할 유망주입니다.",
            },
        ],
    },
    "Cadillac F1 Team": {
        "engine": "Ferrari",
        "base": "Fishers, United States",
        "description": "2026년 그리드에 11번째 팀으로 새롭게 합류한 제너럴 모터스(GM) 산하 캐딜락의 그리드 신규 참여 팀입니다.",
        "drivers": [
            {
                "name": "세르히오 페레스 (Sergio Pérez)",
                "number": "11",
                "nationality": "멕시코",
                "desc": "타이어 관리와 레이스 운영 능력이 탁월한 베테랑 드라이버입니다.",
            },
            {
                "name": "발테리 보타스 (Valtteri Bottas)",
                "number": "77",
                "nationality": "핀란드",
                "desc": "10회 이상의 승리 경험을 바탕으로 신생 팀의 기준을 잡아줄 드라이버입니다.",
            },
        ],
    },
}

schedule_data = [
    {"Round": 1, "Grand Prix": "호주 그랑프리", "Date": "2026-03-08"},
    {"Round": 2, "Grand Prix": "중국 그랑프리", "Date": "2026-03-15"},
    {"Round": 3, "Grand Prix": "일본 그랑프리", "Date": "2026-03-29"},
    {"Round": 4, "Grand Prix": "마이애미 그랑프리", "Date": "2026-05-03"},
    {"Round": 5, "Grand Prix": "캐나다 그랑프리", "Date": "2026-05-24"},
    {"Round": 6, "Grand Prix": "모나코 그랑프리", "Date": "2026-06-07"},
    {
        "Round": 7,
        "Grand Prix": "바르셀로나-카탈루냐 그랑프리",
        "Date": "2026-06-14",
    },
    {"Round": 8, "Grand Prix": "오스트리아 그랑프리", "Date": "2026-06-28"},
    {"Round": 9, "Grand Prix": "영국 그랑프리", "Date": "2026-07-05"},
    {"Round": 10, "Grand Prix": "벨기에 그랑프리", "Date": "2026-07-19"},
    {"Round": 11, "Grand Prix": "헝가리 그랑프리", "Date": "2026-07-26"},
    {"Round": 12, "Grand Prix": "네덜란드 그랑프리", "Date": "2026-08-23"},
    {"Round": 13, "Grand Prix": "이탈리아 그랑프리", "Date": "2026-09-06"},
    {"Round": 14, "Grand Prix": "아제르바이잔 그랑프리", "Date": "2026-09-20"},
    {"Round": 15, "Grand Prix": "싱가포르 그랑프리", "Date": "2026-10-04"},
    {"Round": 16, "Grand Prix": "미국 그랑프리", "Date": "2026-10-18"},
    {"Round": 17, "Grand Prix": "멕시코 그랑프리", "Date": "2026-10-25"},
    {"Round": 18, "Grand Prix": "상파울루 그랑프리", "Date": "2026-11-08"},
    {"Round": 19, "Grand Prix": "라스베이거스 그랑프리", "Date": "2026-11-21"},
    {"Round": 20, "Grand Prix": "카타르 그랑프리", "Date": "2026-11-29"},
    {"Round": 21, "Grand Prix": "아부다비 그랑프리", "Date": "2026-12-06"},
]

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.title("🏁 Navigation")
page = st.sidebar.radio(
    "원하는 메뉴를 선택하세요:", ["팀 및 드라이버 정보", "2026 경기 일정표"]
)

# ---------------------------------------------------------
# Page 1: Teams and Drivers
# ---------------------------------------------------------
if page == "팀 및 드라이버 정보":
    st.subheader("🏎️ 2026 F1 11개 팀 & 드라이버 라인업")

    search_query = st.text_input(
        "🔍 검색할 팀 이름을 입력하세요:", ""
    ).strip()

    filtered_teams = {
        name: data
        for name, data in teams_data.items()
        if search_query.lower() in name.lower()
    }

    if not filtered_teams:
        st.warning("검색 결과가 없습니다.")
    else:
        for team_name, info in filtered_teams.items():
            with st.expander(f"🚩 **{team_name}**", expanded=False):
                st.markdown(
                    f"""
                <div class="card">
                    <h3>{team_name}</h3>
                    <p><b>⚙️ 파워 유닛:</b> {info['engine']}</p>
                    <p><b>📍 베이스:</b> {info['base']}</p>
                    <p>{info['description']}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )

                st.markdown("#### 🏎️ 드라이버 라인업")
                d_col1, d_col2 = st.columns(2)

                for idx, driver in enumerate(info["drivers"]):
                    col = d_col1 if idx == 0 else d_col2
                    with col:
                        st.markdown(
                            f"""
                        <div class="driver-badge">
                            <h4>#{driver['number']} {driver['name']}</h4>
                            <p><b>국적:</b> {driver['nationality']}</p>
                            <p>{driver['desc']}</p>
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )

# ---------------------------------------------------------
# Page 2: Grand Prix Schedule
# ---------------------------------------------------------
else:
    st.subheader("📅 2026 F1 그랑프리 레이스 일정")

    today = datetime.now().date()
    formatted_schedule = []

    for race in schedule_data:
        race_date = datetime.strptime(race["Date"], "%Y-%m-%d").date()
        is_completed = race_date < today

        formatted_schedule.append(
            {
                "라운드": f"Round {race['Round']}",
                "그랑프리": race["Grand Prix"],
                "일자": race["Date"],
                "진행 상태": "✅ 종료됨" if is_completed else "🏁 예정됨",
            }
        )

    df = pd.DataFrame(formatted_schedule)

    # Completed / Upcoming metric displays
    completed_count = sum(1 for r in formatted_schedule if "종료됨" in r["진행 상태"])
    total_count = len(schedule_data)

    m1, m2, m3 = st.columns(3)
    m1.metric("총 라운드 수", f"{total_count} GP")
    m2.metric("진행 완료", f"{completed_count} GP")
    m3.metric("남은 경기", f"{total_count - completed_count} GP")

    st.divider()

    # Highlight Completed Matches using Streamlit Dataframe Styler
    def highlight_completed(val):
        if "종료됨" in str(val):
            return "color: #4CAF50; font-weight: bold"
        return "color: #FF9800; font-weight: bold"

    st.dataframe(
        df.style.applymap(highlight_completed, subset=["진행 상태"]),
        use_container_width=True,
        height=500,
    )
