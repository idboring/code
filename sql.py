import sqlite3

cu = sqlite3.connect("c:/test/ec_zzs.db")
cx = cu.cursor()

#update retailer_census_record

cx.execute("update retailer_census_record set _id = replace(_id, '150921','150925')")
cx.execute("update retailer_census_record set task_id = replace(task_id, '150921','150925')")
cx.execute("update retailer_census_record set qh_code = replace(qh_code, '150921','150925')")
cx.execute("update retailer_census_record set address_building_id = replace(address_building_id, '150921','150925')")
cx.execute("update retailer_census_record set report_datas = replace(cast(report_datas as varchar(8000)), '150921','150925')")

#update company_census_record

cx.execute("update company_census set _id = replace(_id, '150921','150925')")
cx.execute("update company_census set census_id = replace(census_id, '150921','150925')")
cx.execute("update company_census set task_id = replace(task_id, '150921','150925')")
cx.execute("update company_census set qh_code = replace(qh_code, '150921','150925')")
cx.execute("update company_census set address_code = replace(address_code, '150921', '150925')")
cx.execute("update company_census set report_datas = replace(cast(report_datas as varchar(8000)), '150921','150925')")

#update address_bulid_record

cx.execute("update address_bulid set addressCode = replace(addressCode, '150921','150925')")
cx.execute("update address_build set qh_code = replace(qh_code, '150921', '150925')")

cu.commit()
cu.close()


