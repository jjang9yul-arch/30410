import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 페이지 설정
st.set_page_config(
    page_title="F1 2026 World Championship",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. F1 전용 다크 테마 & 하이콘트라스트 화이트 텍스트 CSS 적용
st.markdown("""
    <style>
    /* 전체 배경을 극암색 F1 매트 블랙으로 설정 */
    .stApp {
        background-color: #0b0b0e;
        color: #ffffff !important;
    }
    
    /* 기본 글자색 전체 하얀색으로 강제 고정 */
    html, body, [class*="css"], p, span, label, h1, h2, h3, h4, h5, h6, li, div {
        color: #ffffff !important;
        font-family: 'Titillium Web', 'Pretendard', sans-serif;
    }

    /* 상단 F1 헤더 영역 */
    .f1-header-container {
        text-align: center;
        padding: 20px 0;
        background: linear-gradient(180deg, #181820 0%, #0b0b0e 100%);
        border-bottom: 2px solid #e10600;
        margin-bottom: 25px;
        border-radius: 0 0 15px 15px;
    }
    
    .f1-logo-img {
        width: 260px;
        filter: drop-shadow(0px 0px 10px rgba(225, 6, 0, 0.6));
    }

    /* 카드 스타일 (팀 및 드라이버 카드) */
    .f1-card {
        background: linear-gradient(135deg, #16161e 0%, #1a1a24 100%);
        border: 1px solid #2a2a38;
        border-left: 5px solid #e10600;
        border-radius: 12px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.6), 0 0 15px rgba(225, 6, 0, 0.1);
    }

    .driver-card {
        background-color: #21212b;
        border: 1px solid #333345;
        border-top: 3px solid #e10600;
        border-radius: 10px;
        padding: 18px;
        margin-top: 10px;
        height: 100%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    }

    /* 검색 입력창 스타일링 */
    .stTextInput > div > div > input {
        background-color: #1a1a24 !important;
        color: #ffffff !important;
        border: 1px solid #3a3a4c !important;
        border-radius: 8px !important;
        font-size: 16px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #e10600 !important;
        box-shadow: 0 0 8px rgba(225, 6, 0, 0.5) !important;
    }

    /* 접기/펴기 (Expander) 스타일 조정 */
    .streamlit-expanderHeader {
        background-color: #16161e !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        border: 1px solid #2e2e3e !important;
    }
    .streamlit-expanderContent {
        background-color: #111116 !important;
        border: 1px solid #2e2e3e !important;
        border-top: none !important;
        border-radius: 0 0 8px 8px !important;
    }

    /* 사이드바 다크 스타일 */
    [data-testid="stSidebar"] {
        background-color: #111116;
        border-right: 1px solid #22222d;
    }
    
    /* 강조 텍스트 */
    .highlight-red {
        color: #e10600 !important;
        font-weight: bold;
    }
    .badge-country {
        background-color: #2e2e3e;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 14px;
        color: #00d2be !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 최상단 F1 정식 로고 및 타이틀
st.markdown("""
    <div class="f1-header-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" class="f1-logo-img" alt="F1 Official Logo">
        <h1 style="margin-top: 15px; font-weight: 800; letter-spacing: 2px;">2026 FORMULA 1 WORLD CHAMPIONSHIP</h1>
        <p style="color: #a0a0b0 !important; font-size: 16px;">공식 팀 정보 & 2026 그랑프리 레이스 캘린더</p>
    </div>
""", unsafe_allow_html=True)

# 4. 데이터 정의 (2026 시즌 11개 팀 및 드라이버)
teams_data = {
    "Red Bull Racing": {
        "engine": "Red Bull Ford Powertrains",
        "base": "Milton Keynes, United Kingdom",
        "description": "포드(Ford)와 협력하여 자체 파워유닛 개발에 성공한 레드불 레이싱입니다. 2026년 대대적인 규정 개정 속에서도 기술적 혁신을 이끌어내며 정상 자리를 사수하고 있습니다.",
        "drivers": [
            {"name": "막스 베르스타펜 (Max Verstappen)", "number": "3", "nationality": "🇳🇱 네덜란드", "desc": "압도적인 경기 지배력과 극상의 레이스 페이스를 갖춘 월드 챔피언입니다."},
            {"name": "아이작 하자르 (Isack Hadjar)", "number": "6", "nationality": "🇫🇷 프랑스", "desc": "레드불 주니어 아카데미 출신으로, 날카로운 추월 감각을 보여주는 유망주입니다."}
        ]
    },
    "Ferrari": {
        "engine": "Ferrari",
        "base": "Maranello, Italy",
        "description": "모터스포츠의 전설이자 F1 역사 그 자체인 스쿠데리아 페라리입니다. 고성능 2026 파워유닛과 초호화 드라이버 라인업으로 챔피언십 탈환에 나섭니다.",
        "drivers": [
            {"name": "샤를 르클레르 (Charles Leclerc)", "number": "16", "nationality": "🇲🇨 모나코", "desc": "타의 추종을 불허하는 퀄리파잉 스피드와 정교한 코너링 테크닉을 보유한 페라리의 에이스입니다."},
            {"name": "루이스 해밀턴 (Lewis Hamilton)", "number": "44", "nationality": "🇬🇧 영국", "desc": "F1 7회 월드 챔피언이자 역사상 가장 많은 승리를 거둔 전설적인 드라이버입니다."}
        ]
    },
    "Mercedes": {
        "engine": "Mercedes",
        "base": "Brackley, United Kingdom",
        "description": "엔진 규정 변화 시기마다 강력한 기술력을 증명해 온 메르세데스-AMG입니다. 고효율 파워유닛과 에어로다이내믹 설계를 기반으로 승리를 노립니다.",
        "drivers": [
            {"name": "조지 러셀 (George Russell)", "number": "63", "nationality": "🇬🇧 영국", "desc": "철저한 피드백과 완벽한 정교함을 바탕으로 메르세데스를 지휘하는 리더 드라이버입니다."},
            {"name": "키미 안토넬리 (Kimi Antonelli)", "number": "12", "nationality": "🇮🇹 이탈리아", "desc": "모터스포츠 무대에서 천재적인 감각으로 급부상한 차세대 메르세데스 주니어 출신 드라이버입니다."}
        ]
    },
    "McLaren": {
        "engine": "Mercedes",
        "base": "Woking, United Kingdom",
        "description": "뛰어난 섀시 개발 및 업데이트 스피드로 최근 수년간 최고조의 성장세를 입증한 맥라렌 F1 팀입니다.",
        "drivers": [
            {"name": "랜도 노리스 (Lando Norris)", "number": "1", "nationality": "🇬🇧 영국", "desc": "뛰어난 레이스 페이스와 안정적인 운전 능력으로 맥라렌을 이끄는 에이스 드라이버입니다."},
            {"name": "오스카 피아스트리 (Oscar Piastri)", "number": "81", "nationality": "🇦🇺 호주", "desc": "침착함과 대담한 경기 운영으로 빠르게 최고 수준에 도달한 드라이버입니다."}
        ]
    },
    "Aston Martin": {
        "engine": "Honda",
        "base": "Silverstone, United Kingdom",
        "description": "2026년부터 혼다(Honda)와의 단독 워크스 파트너십을 체결하여 최첨단 실버스톤 캠퍼스에서 타이틀 도전을 선언한 브랜드입니다.",
        "drivers": [
            {"name": "페르난도 알론소 (Fernando Alonso)", "number": "14", "nationality": "🇪🇸 스페인", "desc": "2회 월드 챔피언에 빛나는 압도적인 경험과 레이스IQ를 지닌 베테랑입니다."},
            {"name": "랜스 스트롤 (Lance Stroll)", "number": "18", "nationality": "🇨🇦 캐나다", "desc": "변화무쌍한 웨트 트랙 환경에서 뛰어난 컨트롤 능력을 발휘하는 드라이버입니다."}
        ]
    },
    "Alpine": {
        "engine": "Mercedes",
        "base": "Enstone, United Kingdom",
        "description": "프랑스 알핀의 신기술과 2026년 새로운 메르세데스 파워유닛 패키지를 결합해 중상위권 도약을 노리는 팀입니다.",
        "drivers": [
            {"name": "피에르 개슬리 (Pierre Gasly)", "number": "10", "nationality": "🇫🇷 프랑스", "desc": "그랑프리 우승 이력을 가졌으며 정교한 레이스 주행 능력을 자랑하는 드라이버입니다."},
            {"name": "프랑코 콜라핀토 (Franco Colapinto)", "number": "43", "nationality": "🇦🇷 아르헨티나", "desc": "남미 레이서의 뜨거운 패기와 강렬한 추월 능력을 갖춘 공격적인 신예입니다."}
        ]
    },
    "Williams": {
        "engine": "Mercedes",
        "base": "Grove, United Kingdom",
        "description": "F1 역사상 가장 성공적인 유산 중 하나를 보유한 명문 윌리엄스로, 대규모 시설 투자와 리빌딩을 통해 체질 개선을 완성했습니다.",
        "drivers": [
            {"name": "알렉산더 알본 (Alex Albon)", "number": "23", "nationality": "🇹🇭 태국", "desc": "팀의 리빌딩을 견인해 온 높은 기량과 차량 개발 능력을 인정받은 드라이버입니다."},
            {"name": "카를로스 사인츠 (Carlos Sainz)", "number": "55", "nationality": "🇪🇸 스페인", "desc": "전략적 사고방식과 기복 없는 주행으로 팀의 포인트를 책임지는 드라이버입니다."}
        ]
    },
    "Racing Bulls": {
        "engine": "Red Bull Ford Powertrains",
        "base": "Faenza, Italy",
        "description": "젊고 역동적인 이탈리아 기반의 팀으로, 레드불 파워트레인을 공유하며 민첩한 차량 에어로다이내믹을 자랑합니다.",
        "drivers": [
            {"name": "리암 로슨 (Liam Lawson)", "number": "30", "nationality": "🇳🇿 뉴질랜드", "desc": "과감한 공격 태세와 우수한 타이어 관리 능력을 겸비한 유망주 드라이버입니다."},
            {"name": "아르비드 린드블라드 (Arvid Lindblad)", "number": "41", "nationality": "🇬🇧 영국", "desc": "하위 카테고리를 평정하고 F1 무대에 도전하는 압도적인 스피드의 신예입니다."}
        ]
    },
    "Haas F1 Team": {
        "engine": "Ferrari",
        "base": "Kannapolis, United States",
        "description": "미국 기반의 F1 팀으로 페라리 파워트레인 및 도요타 가주 레이싱(TGR) 기술 제휴를 통해 효율적이고 강력한 차량을 선보입니다.",
        "drivers": [
            {"name": "에스테반 오콘 (Esteban Ocon)", "number": "31", "nationality": "🇫🇷 프랑스", "desc": "단단한 블로킹 능력과 난전 속 기회를 포착하는 철벽 수비형 드라이버입니다."},
            {"name": "올리버 베어먼 (Oliver Bearman)", "number": "87", "nationality": "🇬🇧 영국", "desc": "젊은 에너지를 바탕으로 폭발적인 레이스 페이스를 보여주는 영국의 유망주입니다."}
        ]
    },
    "Audi": {
        "engine": "Audi",
        "base": "Hinwil, Switzerland",
        "description": "자우버 팀 인수를 완료하고 2026년 독자 파워유닛 제작을 통해 최초로 F1에 정식 참전하는 독일의 거대 팩토리 팀 아우디입니다.",
        "drivers": [
            {"name": "니코 휠켄베르크 (Nico Hülkenberg)", "number": "27", "nationality": "🇩🇪 독일", "desc": "초기 신생 워크스 팀 개발 및 세팅에 완벽한 피드백을 선사할 노련한 베테랑입니다."},
            {"name": "가브리에우 보르툴레투 (Gabriel Bortoleto)", "number": "5", "nationality": "🇧🇷 브라질", "desc": "F2/F3 챔피언을 거쳐 아우디의 미래 프로젝트를 이끌어나갈 남미 최고 유망주입니다."}
        ]
    },
    "Cadillac F1 Team": {
        "engine": "Ferrari",
        "base": "Fishers, United States",
        "description": "2026년 그리드에 새롭게 합류한 11번째 팀으로, GM의 캐딜락 브랜드를 등에 업고 글로벌 F1 무대에 화려하게 출사표를 던졌습니다.",
        "drivers": [
            {"name": "세르히오 페레스 (Sergio Pérez)", "number": "11", "nationality": "🇲🇽 멕시코", "desc": "베테랑다운 타이어 마모 관리 능력과 시가지 서킷에서 강력한 모습을 보이는 레이서입니다."},
            {"name": "발테리 보타스 (Valtteri Bottas)", "number": "77", "nationality": "🇫🇮 핀란드", "desc": "10회 이상의 GP 우승 경험으로 캐딜락 팀의 개발과 안정성을 책임집니다."}
        ]
    }
}

# 2026 일정 데이터 (국가 및 도시 정보 추가)
schedule_2026 = [
    {"Round": 1, "Grand Prix": "호주 그랑프리", "Country": "🇦🇺 호주 (멜버른)", "Date": "2026-03-08"},
    {"Round": 2, "Grand Prix": "중국 그랑프리", "Country": "🇨🇳 중국 (상하이)", "Date": "2026-03-15"},
    {"Round": 3, "Grand Prix": "일본 그랑프리", "Country": "🇯🇵 일본 (스즈카)", "Date": "2026-03-29"},
    {"Round": 4, "Grand Prix": "마이애미 그랑프리", "Country": "🇺🇸 미국 (마이애미)", "Date": "2026-05-03"},
    {"Round": 5, "Grand Prix": "캐나다 그랑프리", "Country": "🇨🇦 캐나다 (몬트리올)", "Date": "2026-05-24"},
    {"Round": 6, "Grand Prix": "모나코 그랑프리", "Country": "🇲🇨 모나코 (몬테카를로)", "Date": "2026-06-07"},
    {"Round": 7, "Grand Prix": "카탈루냐 그랑프리", "Country": "🇪🇸 스페인 (바르셀로나)", "Date": "2026-06-14"},
    {"Round": 8, "Grand Prix": "오스트리아 그랑프리", "Country": "🇦🇹 오스트리아 (슈필베르크)", "Date": "2026-06-28"},
    {"Round": 9, "Grand Prix": "영국 그랑프리", "Country": "🇬🇧 영국 (실버스톤)", "Date": "2026-07-05"},
    {"Round": 10, "Grand Prix": "벨기에 그랑프리", "Country": "🇧🇪 벨기에 (스파-프랑코샹)", "Date": "2026-07-19"},
    {"Round": 11, "Grand Prix": "헝가리 그랑프리", "Country": "🇭🇺 헝가리 (부다페스트)", "Date": "2026-07-26"},
    {"Round": 12, "Grand Prix": "네덜란드 그랑프리", "Country": "🇳🇱 네덜란드 (잔트보르트)", "Date": "2026-08-23"},
    {"Round": 13, "Grand Prix": "이탈리아 그랑프리", "Country": "🇮🇹 이탈리아 (몬차)", "Date": "2026-09-06"},
    {"Round": 14, "Grand Prix": "아제르바이잔 그랑프리", "Country": "🇦🇿 아제르바이잔 (바쿠)", "Date": "2026-09-20"},
    {"Round": 15, "Grand Prix": "싱가포르 그랑프리", "Country": "🇸🇬 싱가포르 (마리나베이)", "Date": "2026-10-04"},
    {"Round": 16, "Grand Prix": "미국 그랑프리", "Country": "🇺🇸 미국 (오스틴)", "Date": "2026-10-18"},
    {"Round": 17, "Grand Prix": "멕시코 그랑프리", "Country": "🇲🇽 멕시코 (멕시코시티)", "Date": "2026-10-25"},
    {"Round": 18, "Grand Prix": "상파울루 그랑프리", "Country": "🇧🇷 브라질 (상파울루)", "Date": "2026-11-08"},
    {"Round": 19, "Grand Prix": "라스베이거스 그랑프리", "Country": "🇺🇸 미국 (라스베이거스)", "Date": "2026-11-21"},
    {"Round": 20, "Grand Prix": "카타르 그랑프리", "Country": "🇶🇦 카타르 (루사일)", "Date": "2026-11-29"},
    {"Round": 21, "Grand Prix": "아부다비 그랑프리", "Country": "🇦🇪 아랍에미리트 (야스마리나)", "Date": "2026-12-06"}
]

# 5. 네비게이션 메뉴
st.sidebar.markdown("<h2 style='color: #e10600 !important;'>NAVIGATION</h2>", unsafe_allow_html=True)
menu = st.sidebar.radio(
    "메뉴 선택",
    ["🏎️ F1 팀 & 드라이버 검색", "📅 2026 그랑프리 레이스 일정표"]
)

# ---------------------------------------------------------
# Page 1: 팀 검색 및 드라이버 정보 (검색 시에만 출력)
# ---------------------------------------------------------
if menu == "🏎️ F1 팀 & 드라이버 검색":
    st.markdown("<h2 style='border-bottom: 2px solid #e10600; padding-bottom: 10px;'>SEARCH F1 TEAMS (11 TEAMS)</h2>", unsafe_allow_html=True)
    st.write("")
    
    # 검색어 입력받기
    search_input = st.text_input(
        "🔍 검색할 F1 팀 이름을 입력하세요 (예: Ferrari, Red Bull, Audi, Cadillac 등):", 
        value="",
        placeholder="팀 이름을 입력해야 정보가 표시됩니다."
    ).strip()

    # 검색어가 없는 경우: 미리 표시하지 않고 안내 문구만 출력
    if not search_input:
        st.markdown("""
            <div style="text-align: center; padding: 60px 20px; background-color: #121218; border-radius: 10px; border: 1px dashed #3a3a4c; margin-top: 20px;">
                <h3 style="color: #a0a0b0 !important;">🔍 검색창에 F1 팀명을 입력하세요</h3>
                <p style="color: #707080 !important; margin-top: 10px;">팀명을 검색하면 해당 팀의 2026 시즌 엔진 사양, 베이스, 주요 상세설명 및 드라이버 프로필이 나타납니다.</p>
                <p style="color: #e10600 !important; font-weight: bold; margin-top: 15px;">가능한 11개 팀: Red Bull Racing, Ferrari, Mercedes, McLaren, Aston Martin, Alpine, Williams, Racing Bulls, Haas F1 Team, Audi, Cadillac F1 Team</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        # 검색어 필터링
        filtered_teams = {
            name: data for name, data in teams_data.items()
            if search_input.lower() in name.lower()
        }

        if not filtered_teams:
            st.error(f"❌ '{search_input}'에 해당하는 F1 팀을 찾을 수 없습니다. 정확한 팀명을 입력해주세요.")
        else:
            st.success(f"총 {len(filtered_teams)}개의 팀 검색 결과가 있습니다.")
            
            for team_name, info in filtered_teams.items():
                st.markdown(f"""
                    <div class="f1-card">
                        <h2 style="color: #ffffff !important; margin-bottom: 10px;">🚩 {team_name}</h2>
                        <p style="font-size: 16px; margin-bottom: 5px;"><b style="color: #e10600 !important;">⚙️ 파워 유닛:</b> {info['engine']}</p>
                        <p style="font-size: 16px; margin-bottom: 15px;"><b style="color: #e10600 !important;">📍 팩토리 베이스:</b> {info['base']}</p>
                        <p style="color: #d0d0e0 !important; line-height: 1.6; font-size: 15px;">{info['description']}</p>
                    </div>
                """, unsafe_allow_html=True)

                st.markdown("### 🏎️ DRIVER LINEUP")
                col1, col2 = st.columns(2)

                for idx, driver in enumerate(info["drivers"]):
                    target_col = col1 if idx == 0 else col2
                    with target_col:
                        st.markdown(f"""
                            <div class="driver-card">
                                <h3 style="color: #ffffff !important; margin-bottom: 8px;">
                                    <span style="color: #e10600 !important;">#{driver['number']}</span> {driver['name']}
                                </h3>
                                <p style="font-size: 15px; margin-bottom: 8px;"><b>국적:</b> {driver['nationality']}</p>
                                <hr style="border-color: #333345; margin: 10px 0;">
                                <p style="color: #c0c0d0 !important; font-size: 14px; line-height: 1.5;">{driver['desc']}</p>
                            </div>
                        """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Page 2: 2026 그랑프리 일정표 (국가 구분 및 진행 상태)
# ---------------------------------------------------------
else:
    st.markdown("<h2 style='border-bottom: 2px solid #e10600; padding-bottom: 10px;'>2026 FORMULA 1 RACE CALENDAR</h2>", unsafe_allow_html=True)
    st.write("")

    today = datetime.now().date()
    processed_schedule = []

    for item in schedule_2026:
        race_date = datetime.strptime(item["Date"], "%Y-%m-%d").date()
        is_past = race_date < today
        
        status_text = "✅ 레이스 종료 (DONE)" if is_past else "🏁 진행 예정 (UPCOMING)"
        
        processed_schedule.append({
            "ROUND": f"Round {item['Round']}",
            "그랑프리 명칭": item["Grand Prix"],
            "개최 국가 및 서킷": item["Country"],
            "경기 일자": item["Date"],
            "진행 상태": status_text
        })

    df = pd.DataFrame(processed_schedule)

    # 지표 상자 (Metrics)
    total_races = len(schedule_2026)
    completed_races = sum(1 for r in processed_schedule if "종료" in r["진행 상태"])
    upcoming_races = total_races - completed_races

    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"""
            <div style="background-color: #16161e; padding: 15px; border-radius: 8px; border-top: 3px solid #00d2be; text-align: center;">
                <p style="color: #a0a0b0 !important; margin: 0;">총 그랑프리 수</p>
                <h2 style="color: #ffffff !important; margin: 5px 0;">{total_races} GP</h2>
            </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
            <div style="background-color: #16161e; padding: 15px; border-radius: 8px; border-top: 3px solid #4CAF50; text-align: center;">
                <p style="color: #a0a0b0 !important; margin: 0;">종료된 그랑프리</p>
                <h2 style="color: #4CAF50 !important; margin: 5px 0;">{completed_races} GP</h2>
            </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown(f"""
            <div style="background-color: #16161e; padding: 15px; border-radius: 8px; border-top: 3px solid #e10600; text-align: center;">
                <p style="color: #a0a0b0 !important; margin: 0;">남은 그랑프리</p>
                <h2 style="color: #e10600 !important; margin: 5px 0;">{upcoming_races} GP</h2>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # 테이블 스타일링 커스텀
    def style_status(val):
        if "종료" in str(val):
            return 'background-color: rgba(76, 175, 80, 0.15); color: #4CAF50 !important; font-weight: bold;'
        return 'background-color: rgba(225, 6, 0, 0.15); color: #FF5252 !important; font-weight: bold;'

    styled_df = df.style.map(style_status, subset=['진행 상태'])
    
    st.dataframe(
        styled_df,
        use_container_width=True,
        height=680
    )
