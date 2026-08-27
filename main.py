import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="🏎️ F1 팬 허브 (Formula 1 Fan Hub)",
    page_icon="🏎️",
    layout="wide"
)

# 다크 모드 스타일링 (F1 레이싱 테마)
st.markdown("""
    <style>
    .main-title {
        color: #E10600;
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-title {
        color: #FFFFFF;
        border-left: 5px solid #E10600;
        padding-left: 12px;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .team-info-box {
        background-color: #1f232a;
        padding: 18px;
        border-radius: 10px;
        border: 1px solid #333a46;
        margin-top: 15px;
    }
    .driver-card {
        background-color: #262b35;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
        border-left: 4px solid #E10600;
    }
    </style>
""", unsafe_allow_html=True)

# 2. F1 전체 10개 팀 데이터 (창단연도, 팀 특징, 선수 상세설명 포함)
F1_TEAMS = {
    "레드불 (Red Bull Racing)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Bull_Racing_logo.svg/512px-Red_Bull_Racing_logo.svg.png",
        "founded": "2005년",
        "base": "영국 밀턴킨스",
        "features": "에어로다이내믹스 거장 에드리언 뉴이의 디자인 유산과 막강한 레이스 파워트레인을 바탕으로 2010년대 및 2020년대 초반 F1을 지배한 최고 명문 팀 중 하나입니다.",
        "drivers": [
            {
                "name": "막스 페르스타펜 (Max Verstappen)",
                "no": "1",
                "country": "🇳🇱 네덜란드",
                "bio": "F1 월드 챔피언 출신으로 역대 최연소 F1 데뷔 및 최연소 그랑프리 우승 기록을 보유한 압도적인 드라이빙 테크닉의 소유자입니다."
            },
            {
                "name": "이삭 하드자르 (Isack Hadjar)",
                "no": "6",
                "country": "🇫🇷 프랑스",
                "bio": "레드불 주니어 프로그램 출신의 신예 드라이버로, F2 및 하위 카테고리에서 공격적인 레이스를 선보이며 주목받은 차세대 인재입니다."
            }
        ]
    },
    "페라리 (Scuderia Ferrari)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Ferrari-Logo.svg/380px-Ferrari-Logo.svg.png",
        "founded": "1929년 (F1 참가: 1950년)",
        "base": "이탈리아 마라넬로",
        "features": "F1 출범 첫해인 1950년부터 단 한 번도 빠짐없이 참가한 가장 오래되고 가장 성공적인 F1의 상징적인 명문 붉은 전차 팀입니다.",
        "drivers": [
            {
                "name": "샤를 르클레르 (Charles Leclerc)",
                "no": "16",
                "country": "🇲🇨 모나코",
                "bio": "페라리의 성골 드라이버이자 모나코 국적의 탑 클래스 레이서. 퀄리파잉(예선)에서 독보적인 원랩 스피드를 자랑합니다."
            },
            {
                "name": "루이스 해밀턴 (Lewis Hamilton)",
                "no": "44",
                "country": "🇬🇧 영국",
                "bio": "F1 통산 7회 월드 챔피언 및 역대 최다 우승/폴포지션 기록을 보유한 살아있는 전설. 페라리로 이적하며 큰 화제를 모았습니다."
            }
        ]
    },
    "맥라렌 (McLaren F1 Team)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/McLaren_Racing_logo.svg/512px-McLaren_Racing_logo.svg.png",
        "founded": "1963년",
        "base": "영국 워킹",
        "features": "아일톤 세나, 알랭 프로스트 등 수많은 전설을 배출한 F1 역사의 명가. 최근 유려한 섀시 개발로 다시 정상권 경쟁에 진입했습니다.",
        "drivers": [
            {
                "name": "랜도 노리스 (Lando Norris)",
                "no": "4",
                "country": "🇬🇧 영국",
                "bio": "맥라렌의 프랜차이즈 스타로, 일관된 페이스와 안정적인 주행 능력으로 차세대 챔피언 후보로 꼽힙니다."
            },
            {
                "name": "오스카 피아스트리 (Oscar Piastri)",
                "no": "81",
                "country": "🇦🇺 호주",
                "bio": "F3, F2를 연속 제패하고 F1에 화려하게 데뷔한 침착하고 대담한 레이스운영 능력을 갖춘 슈퍼 루키 출신입니다."
            }
        ]
    },
    "메르세데스 (Mercedes-AMG F1)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Mercedes_AMG_Petronas_F1_Logo.svg/512px-Mercedes_AMG_Petronas_F1_Logo.svg.png",
        "founded": "1954년 (재창단: 2010년)",
        "base": "영국 브랙리",
        "features": "터보 하이브리드 시대(2014~2021)에 8년 연속 컨스트럭터 챔피언이라는 전무후무한 대기록을 작성한 최첨단 엔지니어링의 정점 팀입니다.",
        "drivers": [
            {
                "name": "조지 러셀 (George Russell)",
                "no": "63",
                "country": "🇬🇧 영국",
                "bio": "메르세데스 유스 출신으로 빠른 속도 판단력과 단단한 주행법으로 메르세데스의 새로운 리더 역할을 수행하고 있습니다."
            },
            {
                "name": "키미 안토넬리 (Andrea Kimi Antonelli)",
                "no": "12",
                "country": "🇮🇹 이탈리아",
                "bio": "이탈리아 출신의 초신성 유망주로, 하위 카테고리를 폭속으로 스킵하며 메르세데스 메인 시트를 꿰찬 천재 드라이버입니다."
            }
        ]
    },
    "애스턴 마틴 (Aston Martin)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Aston_Martin_logo.svg/512px-Aston_Martin_logo.svg.png",
        "founded": "2021년 (전신: 포스인디아/레이싱포인트)",
        "base": "영국 실버스톤",
        "features": "영국의 럭셔리 스포츠카 브랜드를 바탕으로 최신 시설의 신규 풍동과 공장을 건설하며 정상권을 목표로 공격적인 투자를 진행 중입니다.",
        "drivers": [
            {
                "name": "페르난도 알론소 (Fernando Alonso)",
                "no": "14",
                "country": "🇪🇸 스페인",
                "bio": "2회 월드 챔피언이자 F1 베테랑. 철저한 관리와 풍부한 경험을 바탕으로 노련하고 뛰어난 레이스 운용을 보여줍니다."
            },
            {
                "name": "랜스 스트롤 (Lance Stroll)",
                "no": "18",
                "country": "🇨🇦 캐나다",
                "bio": "빗길 레이스(Wet Race) 및 스타트 상황에서 깜짝 활약을 보여주는 애스턴 마틴의 주축 드라이버입니다."
            }
        ]
    },
    "알핀 (Alpine F1 Team)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Alpine_F1_Team_Logo.svg/512px-Alpine_F1_Team_Logo.svg.png",
        "founded": "2021년 (전신: 르노 F1)",
        "base": "영국 엔스톤 / 프랑스 비리샤티용",
        "features": "프랑스 르노 그룹의 스포츠카 브랜드 알핀을 대표하며, 견고한 워크스 팀의 인프라를 지니고 있습니다.",
        "drivers": [
            {
                "name": "피에르 가스리 (Pierre Gasly)",
                "no": "10",
                "country": "🇫🇷 프랑스",
                "bio": "2020 이탈리아 GP 우승 경험이 있는 프랑스의 자존심 드라이버. 날카로운 추월 스킬이 장점입니다."
            },
            {
                "name": "프랑코 콜라핀토 (Franco Colapinto)",
                "no": "43",
                "country": "🇦🇷 아르헨티나",
                "bio": "남미 출신의 열정적인 레이서로 뛰어난 적응력과 승부욕을 통해 F1 무대에서 유망한 모습을 보여주고 있습니다."
            }
        ]
    },
    "윌리엄스 (Williams Racing)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Williams_Racing_2020_Logo.svg/512px-Williams_Racing_2020_Logo.svg.png",
        "founded": "1977년",
        "base": "영국 그로브",
        "features": "프랭크 윌리엄스 경에 의해 설립된 전통의 레이싱 전설 팀. 다수의 챔피언십 타이틀을 보유하고 있으며 재건을 도모하고 있습니다.",
        "drivers": [
            {
                "name": "알렉산더 알본 (Alexander Albon)",
                "no": "23",
                "country": "🇹🇭 태국",
                "bio": "윌리엄스의 에이스로 뛰어난 타이어 관리 능력과 한계를 끌어내는 정교한 주행으로 팀의 포인트를 끌어올립니다."
            },
            {
                "name": "카를로스 사인츠 (Carlos Sainz)",
                "no": "55",
                "country": "🇪🇸 스페인",
                "bio": "페라리를 거쳐 윌리엄스에 합류한 베테랑. 뛰어난 엔지니어링 이해도와 명석한 레이스 전략 분석력이 강점입니다."
            }
        ]
    },
    "하스 (Haas F1 Team)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Haas_F1_Team_logo.svg/512px-Haas_F1_Team_logo.svg.png",
        "founded": "2016년",
        "base": "미국 카나폴리스",
        "features": "미국 자본으로 설립된 팀으로, 효율적인 운영 방식과 페라리와의 파트너십을 통해 중위권 싸움에서 효율성을 극대화합니다.",
        "drivers": [
            {
                "name": "에스테반 오콘 (Esteban Ocon)",
                "no": "31",
                "country": "🇫🇷 프랑스",
                "bio": "단단한 수비 주행과 강한 멘탈을 지닌 드라이버로, 2021 헝가리 GP에서 커리어 첫 우승을 기록한 바 있습니다."
            },
            {
                "name": "올리버 베어먼 (Oliver Bearman)",
                "no": "87",
                "country": "🇬🇧 영국",
                "bio": "페라리 드라이버 아카데미 출신으로 긴급 대타 출전에서도 포인트를 획득하며 정식 시트를 확보한 영건입니다."
            }
        ]
    },
    "레이싱 불스 (Racing Bulls / RB)": {
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/Racing_Bulls_logo.svg/512px-Racing_Bulls_logo.svg.png",
        "founded": "2006년 (전신: 토로로소 / 알파타우리)",
        "base": "이탈리아 파엔차",
        "features": "레드불 레이싱의 자매 팀 역할을 하며 신예 드라이버들을 육성하고 빠른 스피드를 검증하는 이탈리아 기반의 팀입니다.",
        "drivers": [
            {
                "name": "리암 로슨 (Liam Lawson)",
                "no": "30",
                "country": "🇳🇿 뉴질랜드",
                "bio": "대타 출전 시기마다 강렬한 임팩트를 남기며 정식 시트를 차지한 공격적인 스타일의 드라이버입니다."
            },
            {
                "name": "아비드 리드블라드 (Arvid Lindblad)",
                "no": "41",
                "country": "🇬🇧 영국",
                "bio": "레드불 청소년 육성 프로그램이 배출한 차세대 루키 드라이버로 높은 성장 가능성을 인정받고 있습니다."
            }
        ]
    },
    "자우버 / 아우디 (Sauber / Audi)": {
        "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Audi-Logo_2016.svg/512px-Audi-Logo_2016.svg.png",
        "founded": "1993년 (자우버)",
        "base": "스위스 힌빌",
        "features": "오랜 역사의 스위스 자우버 팀을 기반으로 독일 명문 브랜드 아우디(Audi)가 인수를 통해 2026년 워크스 팀으로 완전 전환합니다.",
        "drivers": [
            {
                "name": "니코 휠켄베르크 (Nico Hülkenberg)",
                "no": "27",
                "country": "🇩🇪 독일",
                "bio": "F1 무대에서 검증된 탄탄한 기본기와 뛰어난 예선 기록 능력을 보유한 경험 풍부한 베테랑 드라이버입니다."
            },
            {
                "name": "가브리엘 보르톨레토 (Gabriel Bortoleto)",
                "no": "5",
                "country": "🇧🇷 브라질",
                "bio": "F3 챔피언에 이어 F2에서도 독보적인 활약을 펼치며 브라질의 F1 부활을 이끄는 차세대 신성입니다."
            }
        ]
    }
}

# 3. 2026 F1 시즌 한글 일정표 데이터
F1_SCHEDULE_KOREAN = [
    {"round": "제 1 라운드", "gp": "🇦🇺 호주 그랑프리", "circuit": "알버트 파크 서킷 (멜버른)", "date": "3월 6일 ~ 3월 8일"},
    {"round": "제 2 라운드", "gp": "🇨🇳 중국 그랑프리", "circuit": "상하이 인터내셔널 서킷", "date": "3월 13일 ~ 3월 15일"},
    {"round": "제 3 라운드", "gp": "🇯🇵 일본 그랑프리", "circuit": "스즈카 서킷", "date": "3월 27일 ~ 3월 29일"},
    {"round": "제 4 라운드", "gp": "🇺🇸 마이애미 그랑프리", "circuit": "마이애미 인터네셔널 오토드롬", "date": "5월 1일 ~ 5월 3일"},
    {"round": "제 5 라운드", "gp": "🇨🇦 캐나다 그랑프리", "circuit": "질 빌뇌브 서킷 (몬트리올)", "date": "5월 22일 ~ 5월 24일"},
    {"round": "제 6 라운드", "gp": "🇲🇨 모나코 그랑프리", "circuit": "서킷 드 모나코 (몬테카를로)", "date": "6월 5일 ~ 6월 7일"},
    {"round": "제 7 라운드", "gp": "🇪🇸 스페인 바르셀로나 GP", "circuit": "서킷 드 바르셀로나-카탈루냐", "date": "6월 12일 ~ 6월 14일"},
    {"round": "제 8 라운드", "gp": "🇦🇹 오스트리아 그랑프리", "circuit": "레드불 링 (슈필베르크)", "date": "6월 26일 ~ 6월 28일"},
    {"round": "제 9 라운드", "gp": "🇬🇧 영국 그랑프리", "circuit": "실버스톤 서킷", "date": "7월 3일 ~ 7월 5일"},
    {"round": "제 10 라운드", "gp": "🇧🇪 벨기에 그랑프리", "circuit": "스파-프랑코샹 서킷", "date": "7월 17일 ~ 7월 19일"},
    {"round": "제 11 라운드", "gp": "🇭🇺 헝가리 그랑프리", "circuit": "헝가로링 (부다페스트)", "date": "7월 24일 ~ 7월 26일"},
    {"round": "제 12 라운드", "gp": "🇳🇱 네덜란드 그랑프리", "circuit": "잔트보르트 서킷", "date": "8월 21일 ~ 8월 23일"},
    {"round": "제 13 라운드", "gp": "🇮🇹 이탈리아 몬차 GP", "circuit": "몬차 국립 서킷", "date": "9월 4일 ~ 9월 6일"},
    {"round": "제 14 라운드", "gp": "🇪🇸 마드리드 그랑프리", "circuit": "마드리드 스트리트 서킷", "date": "9월 11일 ~ 9월 13일"},
    {"round": "제 15 라운드", "gp": "🇦🇿 아제르바이젠 GP", "circuit": "바쿠 시티 서킷", "date": "9월 24일 ~ 9월 26일"},
    {"round": "제 16 라운드", "gp": "🇸🇬 싱가포르 그랑프리", "circuit": "마리나 베이 스트리트 서킷", "date": "10월 9일 ~ 10월 11일"},
    {"round": "제 17 라운드", "gp": "🇺🇸 미국 오스틴 GP", "circuit": "서킷 오브 디 아메리카스 (COTA)", "date": "10월 23일 ~ 10월 25일"},
    {"round": "제 18 라운드", "gp": "🇲🇽 멕시코 그랑프리", "circuit": "아우토드로모 에르마노스 로드리게스", "date": "10월 30일 ~ 11월 1일"},
    {"round": "제 19 라운드", "gp": "🇧🇷 브라질 상파울루 GP", "circuit": "인테르라고스 서킷", "date": "11월 6일 ~ 11월 8일"},
    {"round": "제 20 라운드", "gp": "🇺🇸 라스베이거스 GP", "circuit": "라스베이거스 스트립 서킷", "date": "11월 19일 ~ 11월 21일"},
    {"round": "제 21 라운드", "gp": "🇶🇦 카타르 그랑프리", "circuit": "루사일 인터내셔널 서킷", "date": "11월 27일 ~ 11월 29일"},
    {"round": "제 22 라운드", "gp": "🇦🇪 아부다비 그랑프리", "circuit": "야스 마리나 서킷", "date": "12월 4일 ~ 12월 6일"}
]

# 화면 상단 타이틀
st.markdown('<div class="main-title">🏎️ FORMULA 1 WORLD CHAMPIONSHIP 🏁</div>', unsafe_allow_html=True)

# 탭 메뉴 구성
tab1, tab2 = st.tabs(["🏎️ 팀 & 드라이버 검색", "📅 시즌 한글 일정표"])

# [TAB 1] 팀 검색 & 드라이버 프로필
with tab1:
    st.markdown('<div class="sub-title">F1 팀 조회 및 드라이버 상세 정보</div>', unsafe_allow_html=True)
    
    selected_team_name = st.selectbox("조회할 F1 팀을 선택하세요:", list(F1_TEAMS.keys()))
    
    if selected_team_name:
        team = F1_TEAMS[selected_team_name]
        
        # 2열 레이아웃 (좌: 로고 및 팀 정보, 우: 드라이버 목록)
        col1, col2 = st.columns([1, 1.4])
        
        with col1:
            # 팀 로고 이미지
            st.image(team["logo"], use_container_width=True)
            
            # 팀 정보 상세 박스
            st.markdown(f"""
                <div class="team-info-box">
                    <h3 style="color:#E10600; margin-top:0;">{selected_team_name}</h3>
                    <p><b>🗓️ 창단 연도:</b> {team['founded']}</p>
                    <p><b>📍 본거지:</b> {team['base']}</p>
                    <hr style="border-color:#444;">
                    <p><b>💡 팀 특징 및 소개:</b><br>{team['features']}</p>
                </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("### 👨‍✈️ 소속 드라이버 라인업")
            st.info("💡 **선수 이름을 클릭하면 상세 설명과 이력이 나옵니다!**")
            
            # 선수별 익스팬더(Expander)로 클릭 시 설명이 펼쳐지도록 구현
            for driver in team["drivers"]:
                with st.expander(f"🏎️ **{driver['name']}** (Car No. {driver['no']})", expanded=False):
                    st.markdown(f"**국적:** {driver['country']}")
                    st.markdown(f"**엔트리 번호:** No. {driver['no']}")
                    st.write("---")
                    st.markdown(f"**📝 드라이버 소개:**")
                    st.write(driver['bio'])

# [TAB 2] 한글 일정표
with tab2:
    st.markdown('<div class="sub-title">2026 F1 레이스 전체 일정 (한글)</div>', unsafe_allow_html=True)
    
    # 레이스 주말 세션안내
    st.caption("ℹ️ F1 레이스 위크엔드는 금요일 연습경기(FP1, FP2), 토요일 예선(Qualifying), 일요일 메인 레이스로 진행됩니다.")
    
    # 2열 카드로 일정 배치
    for i in range(0, len(F1_SCHEDULE_KOREAN), 2):
        col_a, col_b = st.columns(2)
        
        with col_a:
            item = F1_SCHEDULE_KOREAN[i]
            st.markdown(f"""
                <div class="driver-card">
                    <span style="color:#E10600; font-weight:bold;">{item['round']}</span>
                    <h4 style="margin:5px 0;">{item['gp']}</h4>
                    <p style="margin:2px 0; color:#ccc;">📍 {item['circuit']}</p>
                    <p style="margin:2px 0; color:#4dabf7; font-weight:bold;">🗓️ {item['date']}</p>
                </div>
            """, unsafe_allow_html=True)
            
        if i + 1 < len(F1_SCHEDULE_KOREAN):
            with col_b:
                item = F1_SCHEDULE_KOREAN[i+1]
                st.markdown(f"""
                    <div class="driver-card">
                        <span style="color:#E10600; font-weight:bold;">{item['round']}</span>
                        <h4 style="margin:5px 0;">{item['gp']}</h4>
                        <p style="margin:2px 0; color:#ccc;">📍 {item['circuit']}</p>
                        <p style="margin:2px 0; color:#4dabf7; font-weight:bold;">🗓️ {item['date']}</p>
                    </div>
                """, unsafe_allow_html=True)
