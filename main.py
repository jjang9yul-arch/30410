import streamlit as st

st.set_page_config(
    page_title="F1 Official Teams & Drivers",
    page_icon="🏎️",
    layout="wide"
)

# Custom CSS (F1 시그니처 레이싱 테마)
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

# 사진 이미지 속 10개 팀 + 캐딜락 F1 팀 데이터베이스 (각 팀별 고화질 공식 로고 1:1 매칭)
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
                "country": "🇬🇧 United Kingdom",
                "role": "월드 챔피언",
                "desc": "디펜딩 월드 챔피언. 기존 #4번 대신 챔피언의 권리인 #1번을 달고 그리드를 지배 중입니다."
            },
            {
                "name_en": "Oscar Piastri",
                "name_kr": "오스카 피아스트리",
                "number": "81",
                "country": "🇦🇺 Australia",
                "role": "메인 드라이버",
                "desc": "맥라렌의 차세대 에이스. 냉정하고 압도적인 페이스를 자랑합니다."
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
                "country": "🇲🇨 Monaco",
                "role": "메인 드라이버",
                "desc": "페라리의 황태자. 압도적인 예선 퀄리파잉 스피드를 자랑하는 랩 타임의 마술사."
            },
            {
                "name_en": "Lewis Hamilton",
                "name_kr": "루이스 해밀턴",
                "number": "44",
                "country": "🇬🇧 United Kingdom",
                "role": "메인 드라이버",
                "desc": "7회 월드 챔피언. 페라리 레드 슈트를 입고 8번째 타이틀 도전에 나선 전설."
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
                "country": "🇬🇧 United Kingdom",
                "role": "메인 드라이버",
                "desc": "메르세데스 레이싱의 중심축이자 정교한 레이싱 테크닉의 소유자."
            },
            {
                "name_en": "Kimi Antonelli",
                "name_kr": "키미 안토넬리",
                "number": "12",
                "country": "🇮🇹 Italy",
                "role": "루키 드라이버",
                "desc": "실버 애로우의 미래. 세대교체의 중심에 선 유망주."
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
                "country": "🇳🇱 Netherlands",
                "role": "메인 드라이버",
                "desc": "챔피언의 상징 #1 대신 고유 번호 #33으로 탈환에 나선 천재 드라이버."
            },
            {
                "name_en": "Yuki Tsunoda",
                "name_kr": "츠노다 유키",
                "number": "22",
                "country": "🇯🇵 Japan",
                "role": "메인 드라이버",
                "desc": "공격적인 오버테이킹 실력과 배짱을 보유한 드라이버."
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
                "country": "🇹🇭 Thailand",
                "role": "메인 드라이버",
                "desc": "윌리엄스 리빌딩의 일등 공신이자 꾸준한 포인트 획득원."
            },
            {
                "name_en": "Carlos Sainz",
                "name_kr": "카를로스 사인츠",
                "number": "55",
                "country": "🇪🇸 Spain",
                "role": "메인 드라이버",
                "desc": "스페인의 베테랑 전략가. 윌리엄스로 합류하여 팀을 재건 중."
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
                "country": "🇪🇸 Spain",
                "role": "베테랑 챔피언",
                "desc": "F1 역사상 가장 집요하고 공격적인 도그파이트 기술을 가진 살아있는 전설."
            },
            {
                "name_en": "Lance Stroll",
                "name_kr": "랜스 스트롤",
                "number": "18",
                "country": "🇨🇦 Canada",
                "role": "메인 드라이버",
                "desc": "웨트 컨디션에서 뛰어난 감각을 보여주는 드라이버."
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
                "country": "🇩🇪 Germany",
                "role": "베테랑 드라이버",
                "desc": "경험 풍부한 독일 출신 베테랑 머신 세팅 마스터."
            },
            {
                "name_en": "Gabriel Bortoleto",
                "name_kr": "가브리엘 보르톨레토",
                "number": "5",
                "country": "🇧🇷 Brazil",
                "role": "루키 드라이버",
                "desc": "브라질 출신 신성. F3, F2를 석권하고 F1 입성."
            }
        ]
    },
    {
        "team_en": "Visa Cash App RB F1 Team",
        "team_kr": "레이싱 불스 (RB)",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Racing_Bulls_logo.svg",
        "search_keywords": ["레이싱불스", "rb", "리카도", "로슨"],
        "color": "#6692FF",
        "principal": "Laurent Mekies",
        "power_unit": "Honda RBPT",
        "drivers": [
            {
                "name_en": "Liam Lawson",
                "name_kr": "리암 로슨",
                "number": "30",
                "country": "🇳🇿 New Zealand",
                "role": "메인 드라이버",
                "desc": "뉴질랜드 출신의 정교한 드라이빙 스킬을 갖춘 신예."
            },
            {
                "name_en": "Isack Hadjar",
                "name_kr": "아이작 하다르",
                "number": "6",
                "country": "🇫🇷 France",
                "role": "루키 드라이버",
                "desc": "레드불 주니어 프로그램 출신의 공격적인 파이팅을 선보이는 루키."
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
                "country": "🇫🇷 France",
                "role": "메인 드라이버",
                "desc": "하스의 리더로 합류한 집요한 레이스를 펼치는 드라이버."
            },
            {
                "name_en": "Oliver Bearman",
                "name_kr": "올리버 베어만",
                "number": "87",
                "country": "🇬🇧 United Kingdom",
                "role": "루키 드라이버",
                "desc": "대체 출전에서 강렬한 인상을 남기며 시트를 확보한 영국의 미래."
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
                "country": "🇫🇷 France",
                "role": "메인 드라이버",
                "desc": "프랑스 플래그십 팀의 에이스 드라이버."
            },
            {
                "name_en": "Jack Doohan",
                "name_kr": "잭 두한",
                "number": "7",
                "country": "🇦🇺 Australia",
                "role": "루키 드라이버",
                "desc": "F2 무대를 거쳐 승격한 신예 오스트레일리아 드라이버."
            }
        ]
    },
    {
        "team_en": "Cadillac F1 Team",
        "team_kr": "캐딜락 F1 팀 (신규 참전 예정)",
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
                "country": "🇺🇸 USA",
                "role": "시트 확정 대기 중",
                "desc": "신규 11번째 팀 참전에 맞춰 선발될 메인 드라이버."
            },
            {
                "name_en": "TBA Driver 2",
                "name_kr": "미정 드라이버 2",
                "number": "--",
                "country": "🇺🇸 USA",
                "role": "시트 확정 대기 중",
                "desc": "신규 11번째 팀 참전에 맞춰 선발될 메인 드라이버."
            }
        ]
    }
]

# F1 공식 로고
st.markdown("""
    <div class="f1-header-container">
        <img class="f1-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" alt="F1 Logo">
        <div class="f1-logo-text">OFFICIAL GRID & DRIVER VAULT</div>
    </div>
""", unsafe_allow_html=True)

# 검색 및 필터링
col_search, col_filter = st.columns([3, 1])

with col_search:
    search_query = st.text_input(
        "🔍 검색",
        placeholder="팀명(페라리, 맥라렌 등), 드라이버 이름, 번호(#1) 검색...",
        label_visibility="collapsed"
    )

with col_filter:
    team_list = ["전체 팀 보기"] + [t["team_kr"] for t in f1_database]
    selected_team = st.selectbox("팀 선택", team_list, label_visibility="collapsed")

# 검색 처리
filtered_teams = []
query = search_query.strip().lower()

for team in f1_database:
    if selected_team != "전체 팀 보기" and team["team_kr"] != selected_team:
        continue

    if not query:
        filtered_teams.append(team)
    else:
        match_team = any(query in kw.lower() for kw in team["search_keywords"])
        match_driver = any(
            query in d["name_kr"].lower() or 
            query in d["name_en"].lower() or 
            query == d["number"]
            for d in team["drivers"]
        )
        if match_team or match_driver:
            filtered_teams.append(team)

# 팀 및 드라이버 카드 출력
if not filtered_teams:
    st.error(f"'{search_query}' 검색 결과가 없습니다.")
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

        col_logo, col_drivers = st.columns([1, 2.5])

        with col_logo:
            # 전달받은 이미지 속 각 팀의 공식 로고 매칭 출력
            st.image(team["logo_url"], width=180, caption=f"{team['team_kr']} 로고")

        with col_drivers:
            cols = st.columns(len(team["drivers"]))
            for idx, driver in enumerate(team["drivers"]):
                with cols[idx]:
                    with st.popover(f"🏎️ #{driver['number']} {driver['name_kr']}", use_container_width=True):
                        st.markdown(f"### #{driver['number']} {driver['name_kr']}")
                        st.caption(f"{driver['name_en']} | {driver['country']}")
                        st.write(f"**역할:** {driver['role']}")
                        st.info(driver["desc"])

        st.markdown("<hr style='border-color: rgba(255,255,255,0.1); margin: 25px 0;'>", unsafe_allow_html=True)
