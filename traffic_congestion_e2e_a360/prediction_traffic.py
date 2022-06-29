import json
import numpy as np


def predict(artifact_list, payload):
    payload_dict = json.loads(payload)
    model = artifact_list[0]

    feature_names = ['Fastest_Route_Distance', 'Fastest_Route_Time', 'month', 'day_of_month', 'day_of_year', 'week_of_year', 'year', 'is_wknd', 'is_month_start', 'is_month_end', 'Destination_Location_7th_ave', 'Destination_Location_9th_avenue', 'Destination_Location_Al_hateem_palace', 'Destination_Location_D_chowk', 'Destination_Location_IJP road', 'Destination_Location_Jamia Masjid Bilal', 'Destination_Location_air_university', 'Destination_Location_alliedschool_g10', 'Destination_Location_awan_shop', 'Destination_Location_bar_bq_tonight', 'Destination_Location_capital_gymkhana', 'Destination_Location_castpro_engineering', 'Destination_Location_centaurus', 'Destination_Location_childrens_park', 'Destination_Location_crown_plaza', 'Destination_Location_css_officers_academy', 'Destination_Location_dyna_trading_company', 'Destination_Location_eventox_event_management', 'Destination_Location_extreme_engineering_solutions', 'Destination_Location_g9_community_center', 'Destination_Location_geo_news_islamabad_office', 'Destination_Location_gerry_centre', 'Destination_Location_hawks_cricket_ground', 'Destination_Location_horizon_it_networks', 'Destination_Location_hunzapalace', 'Destination_Location_islamabad_model_college_for_boys', 'Destination_Location_italian_pizza', 'Destination_Location_itehad_steel', 'Destination_Location_jamia_masjid', 'Destination_Location_jamia_masjid_sher_e_rabani', 'Destination_Location_jinnah_football_club_ground', 'Destination_Location_kharaian_pull', 'Destination_Location_last_stop', 'Destination_Location_mardan_nursery', 'Destination_Location_mehran hotel', 'Destination_Location_missile_chowk', 'Destination_Location_pak_turk_maarif_international_school', 'Destination_Location_papaya_faroosh', 'Destination_Location_pindora chungi', 'Destination_Location_pirwadhai_masjid', 'Destination_Location_roshan_plaza', 'Destination_Location_salt_and_pepper', 'Destination_Location_talnol_ittehad_plaza', 'Destination_Location_tipu_chowk', 'Destination_Location_wazeer_general_store', 'Destination_Location_zaman_khan_khokha', 'Day_Friday', 'Day_Monday', 'Day_Saturday', 'Day_Sunday', 'Day_Thursday', 'Day_Tuesday', 'Day_Wednesday', 'Fastest_Route_Name_7th Ave', 'Fastest_Route_Name_9th Ave', 'Fastest_Route_Name_A.K. Fazl-ul-Haq Rd', 'Fastest_Route_Name_A.K. Fazl-ul-Haq Rd and Jinnah Ave', 'Fastest_Route_Name_Constitution Ave', 'Fastest_Route_Name_Faisal Ave/Islamabad Expressway', 'Fastest_Route_Name_I.J.P. Rd and I.J.P. Road', 'Fastest_Route_Name_I.J.P. Road', 'Fastest_Route_Name_Ibn-e-Sina Rd', 'Fastest_Route_Name_Ibn-e-Sina Rd and 9th Ave', 'Fastest_Route_Name_Jinnah Ave', 'Fastest_Route_Name_Jinnah Ave and Constitution Ave', 'Fastest_Route_Name_Jinnah Avenue', 'Fastest_Route_Name_Jinnah Avenue and Faisal Avenue Flyover', 'Fastest_Route_Name_Murree Rd and I.J.P. Road', 'Fastest_Route_Name_Nazim-ud-din Rd', 'Fastest_Route_Name_Nazim-ud-din Rd and Jinnah Ave', 'Fastest_Route_Name_Parbat Rd and 7th Ave', 'Fastest_Route_Name_Service Rd E', 'Fastest_Route_Name_Service Rd I 11 (South) and I.J.P. Road', 'Fastest_Route_Name_Service Rd South I 8', 'Fastest_Route_Name_Service Rd W', 'Fastest_Route_Name_Service Rd W and 9th Ave', 'Fastest_Route_Name_Sufi Tabasum Rd', 'Fastest_Route_Name_Sufi Tabasum Rd and Service Rd W', 'Starting_Location_7th_ave', 'Starting_Location_9th_avenue', 'Starting_Location_Al_hateem_palace', 'Starting_Location_Bismillah Hazara Hotel', 'Starting_Location_IJP road', 'Starting_Location_IJP_metro', 'Starting_Location_IJProadstarting_location', 'Starting_Location_STroad_start_stop', 'Starting_Location_air_university', 'Starting_Location_alliedschool_g10', 'Starting_Location_awan_shop', 'Starting_Location_bahria_foundation_school', 'Starting_Location_bar_bq_tonight', 'Starting_Location_capital_gymkhana', 'Starting_Location_castpro_engineering', 'Starting_Location_centaurus', 'Starting_Location_childrens_park', 'Starting_Location_crown_plaza', 'Starting_Location_css_officers_academy', 'Starting_Location_dyna_trading_company', 'Starting_Location_extreme_engineering_solutions', 'Starting_Location_g9_community_center', 'Starting_Location_hawks_cricket_ground', 'Starting_Location_horizon_it_networks', 'Starting_Location_hunzapalace', 'Starting_Location_islamabad_model_college_for_boys', 'Starting_Location_italian_pizza', 'Starting_Location_itehad_steel', 'Starting_Location_jamia_masjid', 'Starting_Location_jamia_masjid_sher_e_rabani', 'Starting_Location_jinnah_football_club_ground', 'Starting_Location_kharaian_pull', 'Starting_Location_mardan_nursery', 'Starting_Location_mehran hotel', 'Starting_Location_missile_chowk', 'Starting_Location_pak_turk_maarif_international_school', 'Starting_Location_papaya_faroosh', 'Starting_Location_pindora', 'Starting_Location_pindora chungi', 'Starting_Location_pirwadhai_masjid', 'Starting_Location_roshan_plaza', 'Starting_Location_salt_and_pepper', 'Starting_Location_talnol_ittehad_plaza', 'Starting_Location_tipu_chowk', 'Starting_Location_wazeer_general_store', 'Starting_Location_zaman_khan_khokha', 'Weather_Clear', 'Weather_Cloudy', 'Weather_Mostly Clear', 'Weather_Mostly Cloudy', 'Weather_Mostly Sunny', 'Weather_Partly Cloudy', 'Weather_Rain', 'Weather_Showers', 'Weather_Sunny' ]

    prediction_list = [payload_dict[feature] for feature in feature_names]
    prediction_vector = np.array(prediction_list).reshape(1, -1)

    prediction = model.predict(prediction_vector)

    return float(prediction[0])