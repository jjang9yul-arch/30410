import streamlit as st

st.set_page_config(
    page_title="F1 Official Grid & Driver Vault",
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

    .f1-header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px 0 25px 0;
        border-bottom: 2px solid rgba(225, 6, 0, 0.4);
        margin-bottom: 25px;
    }

    .f1-logo-img {
        width: 150px;
        filter: drop-shadow(0px 0px 12px rgba(225, 6, 0, 0.8));
        margin-bottom: 12px;
    }

    .f1-logo-text {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.3rem;
        font-weight: 900;
        letter-spacing: 2px;
        background: linear-gradient(90deg, #ffffff, #e10600);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
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
        font-size: 1.6rem;
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

# 10개 팀 + 캐딜락 F1 팀 데이터베이스 (국적, 생년월일, 객관적 프로필 설명 적용)
f1_database = [
    {
        "team_en": "McLaren Formula 1 Team",
        "team_kr": "맥라렌",
        "logo_url": "https://upload.wikimedia.org/wikipedia/en/6/66/McLaren_Racing_logo.svg",
        "search_keywords": ["맥라렌", "mclaren", "노리스", "랜도", "피아스트리", "1", "1번"],
        "color": "#FF8000",
        "principal": "Andrea Stella",
        "power_unit": "Mercedes",
        "drivers": [
            {
                "name_en": "Lando Norris",
                "name_kr": "랜도 노리스",
                "number": "1",
                "country": "영국 (United Kingdom)",
                "birth": "1999년 11월 13일",
                "role": "메인 드라이버",
                "desc": "2019년 맥라렌을 통해 F1에 데뷔했으며, 폴 포지션 및 우승 기록을 보유한 디펜딩 챔피언."
            },
            {
                "name_en": "Oscar Piastri",
                "name_kr": "오스카 피아스트리",
                "number": "81",
                "country": "호주 (Australia)",
                "birth": "2001년 4월 6일",
                "role": "메인 드라이버",
                "desc": "2021년 F2 챔피언 출신으로 2023년 맥라렌에 합류해 루키 시즌부터 스프린트 우승 및 포디움을 기록함."
            }
        ]
    },
    {
        "team_en": "Scuderia Ferrari",
        "team_kr": "페라리",
        "logo_url": "https://upload.wikimedia.org/wikipedia/en/d/d1/Ferrari-Logo.svg",
        "search_keywords": ["페라리", "ferrari", "샤를", "르클레르", "해밀턴", "루이스"],
        "color": "#E8002d",
        "principal": "Frédéric Vasseur",
        "power_unit": "Ferrari",
        "drivers": [
            {
                "name_en": "Charles Leclerc",
                "name_kr": "샤를 르클레르",
                "number": "16",
                "country": "모나코 (Monaco)",
                "birth": "1997년 10월 16일",
                "role": "메인 드라이버",
                "desc": "2018년 자우버로 데뷔 후 2019년부터 스쿠데리아 페라리의 드라이버로 활동 중이며 다수의 퀄리파잉 폴 포지션을 기록함."
            },
            {
                "name_en": "Lewis Hamilton",
                "name_kr": "루이스 해밀턴",
                "number": "44",
                "country": "영국 (United Kingdom)",
                "birth": "1985년 1월 7일",
                "role": "메인 드라이버",
                "desc": "F1 통산 7회 월드 챔피언 달성자로, 맥라렌과 메르세데스를 거쳐 페라리로 이적함."
            }
        ]
    },
    {
        "team_en": "Mercedes-AMG Petronas F1 Team",
        "team_kr": "메르세데스",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Mercedes_AMG_Petronas_F1_Logo.svg",
        "search_keywords": ["메르세데스", "mercedes", "벤츠", "러셀", "안토넬리"],
        "color": "#27F4D2",
        "principal": "Toto Wolff",
        "power_unit": "Mercedes",
        "drivers": [
            {
                "name_en": "George Russell",
                "name_kr": "조지 러셀",
                "number": "63",
                "country": "영국 (United Kingdom)",
                "birth": "1998년 2월 15일",
                "role": "메인 드라이버",
                "desc": "2018년 F2 챔피언 출신으로, 윌리엄스를 거쳐 2022년부터 메르세데스 메인 드라이버로 활동 중."
            },
            {
                "name_en": "Kimi Antonelli",
                "name_kr": "키미 안토넬리",
                "number": "12",
                "country": "이탈리아 (Italy)",
                "birth": "2006년 8월 25일",
                "role": "메인 드라이버",
                "desc": "메르세데스 주니어 프로그램 출신으로, 하위 카테고리를 거쳐 메르세데스 시트를 확보함."
            }
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing",
        "team_kr": "레드불",
        "logo_url": "https://upload.wikimedia.org/wikipedia/en/c/c4/Red_Bull_Racing_logo.svg",
        "search_keywords": ["레드불", "redbull", "막스", "베르스타펜", "페르스타펜", "츠노다"],
        "color": "#3671C6",
        "principal": "Christian Horner",
        "power_unit": "Honda RBPT",
        "drivers": [
            {
                "name_en": "Max Verstappen",
                "name_kr": "막스 베르스타펜",
                "number": "33",
                "country": "네덜란드 (Netherlands)",
                "birth": "1997년 9월 30일",
                "role": "메인 드라이버",
                "desc": "역대 최연소 F1 데뷔 및 최연소 레이스 우승 기록을 보유하고 있는 월드 챔피언."
            },
            {
                "name_en": "Yuki Tsunoda",
                "name_kr": "츠노다 유키",
                "number": "22",
                "country": "일본 (Japan)",
                "birth": "2000년 5월 11일",
                "role": "메인 드라이버",
                "desc": "혼다 드라이버 육성 프로그램 출신으로 2021년 F1 데뷔 후 레드불 레이싱 라인업에 출전."
            }
        ]
    },
    {
        "team_en": "Williams Racing",
        "team_kr": "윌리엄스",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/8/82/Williams_Racing_2020_Logo.svg",
        "search_keywords": ["윌리엄스", "williams", "알본", "사인츠"],
        "color": "#64C4FF",
        "principal": "James Vowles",
        "power_unit": "Mercedes",
        "drivers": [
            {
                "name_en": "Alexander Albon",
                "name_kr": "알렉산더 알본",
                "number": "23",
                "country": "태국 (Thailand)",
                "birth": "1996년 3월 23일",
                "role": "메인 드라이버",
                "desc": "토로 로소와 레드불 레이싱을 거쳐 2022년부터 윌리엄스의 리드 드라이버로 활약 중."
            },
            {
                "name_en": "Carlos Sainz",
                "name_kr": "카를로스 사인츠",
                "number": "55",
                "country": "스페인 (Spain)",
                "birth": "1994년 9월 1일",
                "role": "메인 드라이버",
                "desc": "토로 로소, 르노, 맥라렌, 페라리를 거쳐 윌리엄스로 이적한 베테랑 드라이버."
            }
        ]
    },
    {
        "team_en": "Aston Martin Aramco F1 Team",
        "team_kr": "애스턴 마틴",
        "logo_url": "https://upload.wikimedia.org/wikipedia/en/b/bd/Aston_Martin_Lagonda_brand_logo.svg",
        "search_keywords": ["애스턴마틴", "aston martin", "알론소", "스트롤"],
        "color": "#229971",
        "principal": "Mike Krack",
        "power_unit": "Mercedes",
        "drivers": [
            {
                "name_en": "Fernando Alonso",
                "name_kr": "페르난도 알론소",
                "number": "14",
                "country": "스페인 (Spain)",
                "birth": "1981년 7월 29일",
                "role": "메인 드라이버",
                "desc": "2005년과 2006년 월드 챔피언을 달성했으며 통산 300회 이상의 그랑프리 출전 경력을 보유한 드라이버."
            },
            {
                "name_en": "Lance Stroll",
                "name_kr": "랜스 스트롤",
                "number": "18",
                "country": "캐나다 (Canada)",
                "birth": "1998년 10월 29일",
                "role": "메인 드라이버",
                "desc": "2017년 윌리엄스를 통해 F1에 데뷔한 후 레이싱 포인트를 거쳐 애스턴 마틴에서 활약 중."
            }
        ]
    },
    {
        "team_en": "Stake F1 Team Kick Sauber",
        "team_kr": "킥 자우버",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/0/09/Sauber_Motorsport_logo.svg",
        "search_keywords": ["킥자우버", "자우버", "sauber", "헐켄버그", "보르톨레토"],
        "color": "#52E252",
        "principal": "Mattia Binotto",
        "power_unit": "Ferrari",
        "drivers": [
            {
                "name_en": "Nico Hülkenberg",
                "name_kr": "니코 훌켄버그",
                "number": "27",
                "country": "독일 (Germany)",
                "birth": "1987년 8월 19일",
                "role": "메인 드라이버",
                "desc": "2010년 데뷔 이래 다양한 팀에서 활동했으며 높은 레이스 운영 능력을 지닌 독일 출신 드라이버."
            },
            {
                "name_en": "Gabriel Bortoleto",
                "name_kr": "가브리엘 보르톨레토",
                "number": "5",
                "country": "브라질 (Brazil)",
                "birth": "2004년 10월 14일",
                "role": "메인 드라이버",
                "desc": "2023년 F3 챔피언을 기록한 후 자우버 팀을 통해 F1에 정식 입성함."
            }
        ]
    },
    {
        "team_en": "Visa Cash App RB F1 Team",
        "team_kr": "레이싱 불스 (RB)",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Racing_Bulls_logo.svg",
        "search_keywords": ["레이싱불스", "rb", "로슨", "하다르"],
        "color": "#6692FF",
        "principal": "Laurent Mekies",
        "power_unit": "Honda RBPT",
        "drivers": [
            {
                "name_en": "Liam Lawson",
                "name_kr": "리암 로슨",
                "number": "30",
                "country": "뉴질랜드 (New Zealand)",
                "birth": "2002년 2월 11일",
                "role": "메인 드라이버",
                "desc": "레드불 주니어 팀 출신으로 2023년 리저브 드라이버로 대타 출전 후 정식 시트를 확보함."
            },
            {
                "name_en": "Isack Hadjar",
                "name_kr": "아이작 하다르",
                "number": "6",
                "country": "프랑스 (France)",
                "birth": "2004년 9월 28일",
                "role": "메인 드라이버",
                "desc": "레드불 주니어 프로그램 출신으로 F2에서 뛰어난 성적을 올린 뒤 레이싱 불스에 합류함."
            }
        ]
    },
    {
        "team_en": "MoneyGram Haas F1 Team",
        "team_kr": "하스",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Haas_F1_Team_logo.svg",
        "search_keywords": ["하스", "haas", "오콘", "베어만"],
        "color": "#B6BABD",
        "principal": "Ayao Komatsu",
        "power_unit": "Ferrari",
        "drivers": [
            {
                "name_en": "Esteban Ocon",
                "name_kr": "에스테반 오콘",
                "number": "31",
                "country": "프랑스 (France)",
                "birth": "1996년 9월 17일",
                "role": "메인 드라이버",
                "desc": "2016년 데뷔 후 2021년 헝가리 그랑프리에서 첫 승을 기록하였으며 하스 팀으로 이적함."
            },
            {
                "name_en": "Oliver Bearman",
                "name_kr": "올리버 베어만",
                "number": "87",
                "country": "영국 (United Kingdom)",
                "birth": "2005년 5월 8일",
                "role": "메인 드라이버",
                "desc": "페라리 드라이버 아카데미 출신으로 2024년 페라리 대타 출전에서 포인트를 획득하고 하스 정식 드라이버로 계약함."
            }
        ]
    },
    {
        "team_en": "Alpine F1 Team",
        "team_kr": "알핀",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Alpine_F1_Team_Logo.svg",
        "search_keywords": ["알핀", "alpine", "가슬리", "두한"],
        "color": "#0093CC",
        "principal": "Oliver Oakes",
        "power_unit": "Renault",
        "drivers": [
            {
                "name_en": "Pierre Gasly",
                "name_kr": "피에르 가슬리",
                "number": "10",
                "country": "프랑스 (France)",
                "birth": "1996년 2월 7일",
                "role": "메인 드라이버",
                "desc": "2020년 이탈리아 그랑프리 우승을 기록한 바 있으며 2023년부터 알핀 메인 드라이버로 활약 중."
            },
            {
                "name_en": "Jack Doohan",
                "name_kr": "잭 두한",
                "number": "7",
                "country": "호주 (Australia)",
                "birth": "2003년 1월 20일",
                "role": "메인 드라이버",
                "desc": "알핀 아카데미 출신 드라이버로 F2 무대를 거쳐 알핀의 정식 드라이버로 승격함."
            }
        ]
    },
    {
        "team_en": "Cadillac F1 Team",
        "team_kr": "캐딜락 F1 팀",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Cadillac_logo.svg",
        "search_keywords": ["캐딜락", "cadillac", "11번째"],
        "color": "#FFD700",
        "principal": "미정 (TBA)",
        "power_unit": "GM / Ferrari",
        "drivers": [
            {
                "name_en": "TBA Driver 1",
                "name_kr": "미정 드라이버 1",
                "number": "--",
                "country": "미정",
                "birth": "미정",
                "role": "시트 확정 대기 중",
                "desc": "신규 11번째 팀 참전에 맞춰 선발될 예정인 드라이버."
            },
            {
                "name_en": "TBA Driver 2",
                "name_kr": "미정 드라이버 2",
                "number": "--",
                "country": "미정",
                "birth": "미정",
                "role": "시트 확정 대기 중",
                "desc": "신규 11번째 팀 참전에 맞춰 선발될 예정인 드라이버."
            }
        ]
    }
]

# F1 공식 로고 및 타이틀 Header
st.markdown("""
    <div class="f1-header-container">
        <img class="f1-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" alt="F1 Logo">
        <div class="f1-logo-text">OFFICIAL GRID & DRIVER VAULT</div>
    </div>
""", unsafe_allow_html=True)

# 검색 및 드롭다운 선택 (요청에 따라 '전체 보기' 옵션 제거)
col_search, col_filter = st.columns([3, 1])

with col_search:
    search_query = st.text_input(
        "🔍 검색",
        placeholder="팀명(페라리, 맥라렌 등), 드라이버 이름, 번호(#1) 검색...",
        label_visibility="collapsed"
    )

with col_filter:
    # '전체 보기' 제거 후 첫 번째 팀(맥라렌)을 기본 선택으로 설정
    team_list = [t["team_kr"] for t in f1_database]
    selected_team = st.selectbox("팀 선택", team_list, label_visibility="collapsed")

# 필터링 로직 (검색어가 없으면 선택된 팀만 표시)
filtered_teams = []
query = search_query.strip().lower()

for team in f1_database:
    if query:
        match_team = any(query in kw.lower() for kw in team["search_keywords"])
        match_driver = any(
            query in d["name_kr"].lower() or 
            query in d["name_en"].lower() or 
            query == d["number"]
            for d in team["drivers"]
        )
        if match_team or match_driver:
            filtered_teams.append(team)
    else:
        if team["team_kr"] == selected_team:
            filtered_teams.append(team)

# 팀 및 드라이버 정보 출력
if not filtered_teams:
    st.error(f"'{search_query}'에 대한 검색 결과가 없습니다.")
else:
    for team in filtered_teams:
        st.markdown(f"""
            <div class="team-card" style="border-top: 4px solid {team['color']};">
                <div class="team-title" style="color: {team['color']};">{team['team_en']} ({team['team_kr']})</div>
                <div style="margin-top: 6px;">
                    <span class="stat-badge">감독: {team['principal']}</span>
                    <span class="stat-badge">파워유닛: {team['power_unit']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        cols = st.columns(len(team["drivers"]))
        for idx, driver in enumerate(team["drivers"]):
            with cols[idx]:
                with st.popover(f"🏎️ #{driver['number']} {driver['name_kr']}", use_container_width=True):
                    st.markdown(f"### #{driver['number']} {driver['name_kr']}")
                    st.caption(f"{driver['name_en']}")
                    st.write(f"**국적:** {driver['country']}")
                    st.write(f"**생년월일:** {driver['birth']}")
                    st.write(f"**역할:** {driver['role']}")
                    st.info(driver["desc"])

        st.markdown("<hr style='border-color: rgba(255,255,255,0.1); margin: 25px 0;'>", unsafe_allow_html=True)
        # Streamlit 앱용 2026 F1 일정 데이터 세트
f1_schedule_2026 = [
    {"round": 1, "country": "🇦🇺 오스트레일리아", "circuit": "앨버트 파크 서킷", "city": "멜버른", "date": "2026. 03. 08"},
    {"round": 2, "country": "🇨🇳 중국", "circuit": "상하이 인터내셔널 서킷", "city": "상하이", "date": "2026. 03. 15"},
    {"round": 3, "country": "🇯🇵 일본", "circuit": "스즈카 서킷", "city": "스즈카", "date": "2026. 03. 29"},
    {"round": 4, "country": "🇺🇸 미국", "circuit": "마이애미 인터내셔널 오토드로름", "city": "마이애미", "date": "2026. 05. 03"},
    {"round": 5, "country": "🇨🇦 캐나다", "circuit": "서킷 질 빌뇌브", "city": "몬트리올", "date": "2026. 05. 24"},
    {"round": 6, "country": "🇲🇨 모나코", "circuit": "서킷 드 모나코", "city": "몬테카를로", "date": "2026. 06. 07"},
    {"round": 7, "country": "🇪🇸 스페인", "circuit": "서킷 드 바르셀로나-카탈루냐", "city": "바르셀로나", "date": "2026. 06. 14"},
    {"round": 8, "country": "🇦🇹 오스트리아", "circuit": "레드불 링", "city": "슈필베르크", "date": "2026. 06. 28"},
    {"round": 9, "country": "🇬🇧 영국", "circuit": "실버스톤 서킷", "city": "실버스톤", "date": "2026. 07. 05"},
    {"round": 10, "country": "🇧🇪 벨기에", "circuit": "스파-프랑코샹 서킷", "city": "스파", "date": "2026. 07. 19"},
    {"round": 11, "country": "🇭🇺 헝가리", "circuit": "헝가로링", "city": "부다페스트", "date": "2026. 07. 26"},
    {"round": 12, "country": "🇳🇱 네덜란드", "circuit": "잔트포르트 서킷", "city": "잔트포르트", "date": "2026. 08. 23"},
    {"round": 13, "country": "🇮🇹 이탈리아", "circuit": "오토드로모 나치오날레 몬차", "city": "몬차", "date": "2026. 09. 06"},
    {"round": 14, "country": "🇪🇸 스페인", "circuit": "마드리드 스트리트 서킷", "city": "마드리드", "date": "2026. 09. 13"},
    {"round": 15, "country": "🇦🇿 아제르바이잔", "circuit": "바쿠 시티 서킷", "city": "바쿠", "date": "2026. 09. 26"},
    {"round": 16, "country": "🇸🇬 싱가포르", "circuit": "마리나 베이 스트리트 서킷", "city": "싱가포르", "date": "2026. 10. 11"},
    {"round": 17, "country": "🇺🇸 미국", "circuit": "서킷 오브 디 아메리카스", "city": "오스틴", "date": "2026. 10. 25"},
    {"round": 18, "country": "🇲🇽 멕시코", "circuit": "오토드로모 에르마노스 로드리게스", "city": "멕시코시티", "date": "2026. 11. 01"},
    {"round": 19, "country": "🇧🇷 브라질", "circuit": "호세 카를로스 파체 서킷 (인터라고스)", "city": "상파울루", "date": "2026. 11. 08"},
    {"round": 20, "country": "🇺🇸 미국", "circuit": "라스베이거스 스트립 서킷", "city": "라스베이거스", "date": "2026. 11. 21"},
    {"round": 21, "country": "🇶🇦 카타르", "circuit": "루사일 인터내셔널 서킷", "city": "루사일", "date": "2026. 11. 29"},
    {"round": 22, "country": "🇦🇪 아랍에미리트", "circuit": "야스 마리나 서킷", "city": "아부다비", "date": "2026. 12. 06"}
]

# Streamlit에 표 형태로 출력하기
import streamlit as st
import pandas as pd

st.title("🏎️ 2026 F1 그랑프리 일정표")
df_schedule = pd.DataFrame(f1_schedule_2026)
st.dataframe(
    df_schedule.rename(columns={
        "round": "라운드", 
        "country": "국가", 
        "circuit": "서킷 명칭", 
        "city": "도시", 
        "date": "결승 날짜"
    }), 
    use_container_width=True,
    hide_index=True
)
