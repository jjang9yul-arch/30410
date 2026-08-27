import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="F1 Grid & Driver Vault",
    page_icon="🏎️",
    layout="wide"
)

# Custom CSS (F1 레이싱 테마 + 로고 애니메이션 및 카드 스타일)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    /* 전체 배경 */
    .stApp {
        background: linear-gradient(135deg, #0b0e14 0%, #151a24 50%, #05070a 100%);
        color: #f3f4f6;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* 상단 Flow / 헤더 영역 (F1 로고 포함) */
    .f1-header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px 0 30px 0;
        border-bottom: 2px solid rgba(225, 6, 0, 0.4);
        margin-bottom: 30px;
    }

    .f1-logo-img {
        width: 160px;
        filter: drop-shadow(0px 0px 15px rgba(225, 6, 0, 0.8));
        margin-bottom: 15px;
    }

    .f1-logo-text {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        font-weight: 900;
        letter-spacing: 3px;
        background: linear-gradient(90deg, #ffffff, #e10600);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* 팀 카드 */
    .team-card {
        background: rgba(21, 26, 36, 0.85);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
    }

    .team-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.8rem;
        font-weight: 800;
    }

    /* 드라이버 카드 */
    .driver-card {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .driver-number {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.2rem;
        font-weight: 900;
        color: #e10600;
        line-height: 1;
        min-width: 55px;
    }

    .driver-name {
        font-size: 1.2rem;
        font-weight: 700;
        color: #ffffff;
    }

    .stat-badge {
        display: inline-block;
        background: rgba(225, 6, 0, 0.2);
        border: 1px solid rgba(225, 6, 0, 0.5);
        color: #ff4d4d;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 2026 최신 데이터베이스 (Lando Norris #1 반영 및 안정적인 고화질 사진 주소 사용)
f1_database = [
    {
        "team_en": "McLaren Formula 1 Team",
        "team_kr": "맥라렌",
        "search_keywords": ["맥라렌", "mclaren", "노리스", "랜도", "피아스트리", "1", "1번"],
        "color": "#FF8000",
        "principal": "Andrea Stella",
        "power_unit": "Mercedes",
        "car_img": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?q=80&w=1000&auto=format&fit=crop",
        "drivers": [
            {
                "name_en": "Lando Norris",
                "name_kr": "랜도 노리스",
                "number": "1",  # 챔피언 등극으로 1번 사용
                "country": "🇬🇧 United Kingdom",
                "role": "월드 챔피언 (World Champion)",
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Lando_Norris_2019.jpg/800px-Lando_Norris_2019.jpg",
                "desc": "디펜딩 월드 챔피언. 기존 #4번 대신 챔피언의 권리인 #1번을 달고 그리드를 지배 중."
            },
            {
                "name_en": "Oscar Piastri",
                "name_kr": "오스카 피아스트리",
                "number": "81",
                "country": "🇦🇺 Australia",
                "role": "메인 드라이버",
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Oscar_Piastri_2023.jpg/800px-Oscar_Piastri_2023.jpg",
                "desc": "맥라렌의 강력한 듀얼 에이스. 완벽한 냉정함과 폭발적인 스피드를 겸비한 드라이버."
            }
        ]
    },
    {
        "team_en": "Scuderia Ferrari",
        "team_kr": "스크루데리아 페라리",
        "search_keywords": ["페라리", "ferrari", "샤를", "르클레르", "해밀턴", "루이스"],
        "color": "#E8002d",
        "principal": "Frédéric Vasseur",
        "power_unit": "Ferrari",
        "car_img": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?q=80&w=1000&auto=format&fit=crop",
        "drivers": [
            {
                "name_en": "Charles Leclerc",
                "name_kr": "샤를 르클레르",
                "number": "16",
                "country": "🇲🇨 Monaco",
                "role": "메인 드라이버",
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Charles_Leclerc_2022.jpg/800px-Charles_Leclerc_2022.jpg",
                "desc": "페라리의 성골 에이스. 폴 포지션 타임의 마술사이자 붉은 제국의 핵심."
            },
            {
                "name_en": "Lewis Hamilton",
                "name_kr": "루이스 해밀턴",
                "number": "44",
                "country": "🇬🇧 United Kingdom",
                "role": "메인 드라이버",
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Lewis_Hamilton_2022_At_Silverstone.jpg/800px-Lewis_Hamilton_2022_At_Silverstone.jpg",
                "desc": "7회 월드 챔피언. 페라리 레드 슈트를 입고 8번째 타이틀을 향해 달리는 레이싱 전설."
            }
        ]
    },
    {
        "team_en": "Oracle Red Bull Racing",
        "team_kr": "레드불 레이싱",
        "search_keywords": ["레드불", "redbull", "red bull", "막스", "베르스타펜", "페르스타펜", "츠노다"],
        "color": "#3671C6",
        "principal": "Christian Horner",
        "power_unit": "Honda RBPT",
        "car_img": "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?q=80&w=1000&auto=format&fit=crop",
        "drivers": [
            {
                "name_en": "Max Verstappen",
                "name_kr": "막스 베르스타펜",
                "number": "33",  # #1번 내려놓고 원래 번호 #33 복귀
                "country": "🇳🇱 Netherlands",
                "role": "메인 드라이버",
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Max_Verstappen_2017_Malaysia.jpg/800px-Max_Verstappen_2017_Malaysia.jpg",
                "desc": "챔피언의 상징 #1 대신 고유 번호 #33으로 탈환에 나선 천재 드라이버."
            },
            {
                "name_en": "Yuki Tsunoda",
                "name_kr": "츠노다 유키",
                "number": "22",
                "country": "🇯🇵 Japan",
                "role": "메인 드라이버",
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Yuki_Tsunoda_2021_AISC.jpg/800px-Yuki_Tsunoda_2021_AISC.jpg",
                "desc": "공격적인 오버테이킹 실력과 압도적인 배짱을 보여주는 드라이버."
            }
        ]
    },
    {
        "team_en": "Mercedes-AMG Petronas F1 Team",
        "team_kr": "메르세데스 AMG",
        "search_keywords": ["메르세데스", "mercedes", "벤츠", "러셀", "안토넬리"],
        "color": "#27F4D2",
        "principal": "Toto Wolff",
        "power_unit": "Mercedes",
        "car_img": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?q=80&w=1000&auto=format&fit=crop",
        "drivers": [
            {
                "name_en": "George Russell",
                "name_kr": "조지 러셀",
                "number": "63",
                "country": "🇬🇧 United Kingdom",
                "role": "메인 드라이버",
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/George_Russell_2019.jpg/800px-George_Russell_2019.jpg",
                "desc": "메르세데스 레이싱의 중심축이자 안정적인 페이스 조절의 일인자."
            },
            {
                "name_en": "Kimi Antonelli",
                "name_kr": "키미 안토넬리",
                "number": "12",
                "country": "🇮🇹 Italy",
                "role": "루키 드라이버",
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Andrea_Kimi_Antonelli_2024.jpg/800px-Andrea_Kimi_Antonelli_2024.jpg",
                "desc": "실버 애로우의 미래. 세대교체의 중심에 선 차세대 유망주."
            }
        ]
    }
]

# 1. 상단 Header / Flow 영역 (공식 F1 로고 적용)
st.markdown("""
    <div class="f1-header-container">
        <img class="f1-logo-img" src="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" alt="F1 Logo">
        <div class="f1-logo-text">GRID & DRIVER VAULT</div>
        <div style="color: #9ca3af; font-size: 1rem; margin-top: 5px;">공식 F1 팀 및 드라이버 검색 가이드</div>
    </div>
""", unsafe_allow_html=True)

# 2. 검색창 레이아웃
col_search, col_filter = st.columns([3, 1])

with col_search:
    search_query = st.text_input(
        "🔍 검색어를 입력하세요",
        placeholder="예: 페라리, 랜도 노리스, 1번, 레드불, 해밀턴...",
        label_visibility="collapsed"
    )

with col_filter:
    team_list = ["전체 팀 보기"] + [t["team_kr"] for t in f1_database]
    selected_team = st.selectbox("팀 선택", team_list, label_visibility="collapsed")

# 3. 검색 알고리즘
filtered_teams = []
query = search_query.strip().lower()

for team in f1_database:
    if selected_team != "전체 팀 보기" and team["team_kr"] != selected_team:
        continue

    if not query:
        filtered_teams.append(team)
    else:
        # 키워드/번호/이름 검색
        match_team = any(query in kw.lower() for kw in team["search_keywords"])
        match_driver = any(
            query in d["name_kr"].lower() or 
            query in d["name_en"].lower() or 
            query == d["number"]
            for d in team["drivers"]
        )
        if match_team or match_driver:
            filtered_teams.append(team)

# 4. 결과 출력
if not filtered_teams:
    st.error(f"'{search_query}'에 대한 검색 결과가 없습니다. 팀명(예: 페라리)이나 드라이버 이름, 번호(#1)를 검색해보세요.")
else:
    for team in filtered_teams:
        st.markdown(f"""
            <div class="team-card" style="border-top: 4px solid {team['color']};">
                <div class="team-title" style="color: {team['color']};">{team['team_en']}</div>
                <div style="font-size: 1.1rem; color: #d1d5db; margin-bottom: 12px;">{team['team_kr']}</div>
                <div>
                    <span class="stat-badge">감독: {team['principal']}</span>
                    <span class="stat-badge">파워유닛: {team['power_unit']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        col_car, col_drivers = st.columns([1.2, 2])

        with col_car:
            st.image(team["car_img"], caption=f"{team['team_kr']} 머신", use_container_width=True)

        with col_drivers:
            for driver in team["drivers"]:
                d_col1, d_col2 = st.columns([1, 3])
                with d_col1:
                    st.image(driver["img"], width=110)
                with d_col2:
                    st.markdown(f"""
                        <div class="driver-card" style="border-left: 4px solid {team['color']};">
                            <div class="driver-number">#{driver['number']}</div>
                            <div>
                                <div class="driver-name">{driver['name_kr']} <span style="font-size:0.85rem; color:#9ca3af;">({driver['name_en']})</span></div>
                                <div style="font-size: 0.85rem; color: #9ca3af;">{driver['country']} • {driver['role']}</div>
                                <div style="font-size: 0.85rem; color: #d1d5db; margin-top: 4px;">{driver['desc']}</div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
        
        st.markdown("<hr style='border-color: rgba(255,255,255,0.1); margin: 30px 0;'>", unsafe_allow_html=True)
