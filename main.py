import streamlit as st

# 1. 페이지 설정 (와이드 모드)
st.set_page_config(page_title="F1 2026 Hub", page_icon="🏎️", layout="wide")

# 2. 상단 F1 로고 및 타이틀
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg", width=250
)
st.title("F1 2026 시즌 통합 정보 포털")
st.markdown("---")

# 사이드바 메뉴
menu = st.sidebar.selectbox(
    "메뉴 선택", ["홈 & 팀 검색", "2026 전체 팀 & 드라이버", "2026 레이스 일정 & 포디움"]
)

# 샘플 데이터 (2026년 기준 주요 팀 및 드라이버 예시)
f1_data = {
    "Ferrari": {
        "desc": "이탈리아의 자존심, 모터스포츠의 전설적인 프랜차이즈 팀",
        "drivers": [
            {
                "name": "Charles Leclerc",
                "nat": "모나코 🇲🇨",
                "dob": "1997.10.16",
            },
            {
                "name": "Lewis Hamilton",
                "nat": "영국 🇬🇧",
                "dob": "1985.01.07",
            },
        ],
    },
    "Mercedes": {
        "desc": "파워유닛 시대의 강자, 혁신을 거듭하는 은빛 화살",
        "drivers": [
            {"name": "George Russell", "nat": "영국 🇬🇧", "dob": "1998.02.15"},
            {
                "name": "Kimi Antonelli",
                "nat": "이탈리아 🇮🇹",
                "dob": "2006.08.25",
            },
        ],
    },
}

# 3. 홈 & 팀 검색 기능
if menu == "홈 & 팀 검색":
    st.header("🔍 F1 팀 및 드라이버 통합 검색")
    search_query = st.text_input(
        "찾고 싶은 팀 이름을 입력하세요 (예: Ferrari, Mercedes):"
    )

    if search_query:
        found = False
        for team, info in f1_data.items():
            if search_query.lower() in team.lower():
                found = True
                st.subheader(f"🔴 {team}")
                st.write(info["desc"])
                st.markdown("### 소속 드라이버")
                for d in info["drivers"]:
                    st.info(
                        f"**{d['name']}** | 국적: {d['nat']} | 생년월일: {d['dob']}"
                    )
        if not found:
            st.warning("검색 결과가 없습니다. 팀 이름을 다시 확인해 주세요!")

# 4. 전체 팀 & 드라이버 소개
elif menu == "2026 전체 팀 & 드라이버":
    st.header("🏁 2026 시즌 팀 & 드라이버 라인업")
    for team, info in f1_data.items():
        with st.expander(f"🏎️ {team} 팀 정보 보기"):
            st.write(f"**팀 소개:** {info['desc']}")
            col1, col2 = st.columns(2)
            for i, d in enumerate(info["drivers"]):
                with col1 if i == 0 else col2:
                    st.success(
                        f"**드라이버:** {d['name']}\n\n- 국적: {d['nat']}\n- 생년월일: {d['dob']}"
                    )

# 5. 2026 레이스 일정 및 포디움
elif menu == "2026 레이스 일정 & 포디움":
    st.header("📅 2026 FIA 포뮬러 원 월드 챔피언십 일정")

    # 예시 일정표 데이터 (완료된 경기 vs 예정된 경기)
    schedule = [
        {
            "Round": 1,
            "Grand Prix": "Bahrain GP",
            "Date": "2026.03.02",
            "Status": "종료",
            "Podium": "1위: C. Leclerc\n2위: L. Hamilton\n3위: M. Verstappen",
        },
        {
            "Round": 2,
            "Grand Prix": "Saudi Arabian GP",
            "Date": "2026.03.09",
            "Status": "종료",
            "Podium": "1위: G. Russell\n2위: C. Leclerc\n3위: L. Norris",
        },
        {
            "Round": 3,
            "Grand Prix": "Australian GP",
            "Date": "2026.03.23",
            "Status": "예정",
            "Podium": "경기 전",
        },
    ]

    for item in schedule:
        col1, col2, col3 = st.columns([1, 2, 3])
        with col1:
            st.markdown(f"**R{item['Round']}**")
        with col2:
            st.markdown(f"**{item['Grand Prix']}**\n\n일정: {item['Date']}")
        with col3:
            if item["Status"] == "종료":
                st.error(f"🏆 **포디움 결과**\n\n{item['Podium']}")
            else:
                st.info(f"⏳ **상태:** {item['Status']} (레이스 대기 중)")
        st.markdown("---")
