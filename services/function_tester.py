de_prov_payload = {'identity': {'identity_id': '3409d68329d7304a1d5b95658c405e62', 'create_ts': '2023-03-18 19:08:11.160', 'hr_id': '49', 'user_id': 'robert.m.hartman49', 'legal_first_name': 'robert', 'legal_middle_name': 'maurice', 'legal_last_name': 'hartman', 'preferred_first_name': 'robert', 'preferred_middle_name': 'maurice', 'preferred_last_name': 'hartman', 'use_preferred_name': 'false', 'job_title_code': 'eng', 'job_title_description': 'eng', 'job_title_level': '100', 'location_code': '1001', 'location_name': 'norfolk', 'email_work_primary': 'robert.hartman@hartmancorp.com', 'status': 'A', 'hire_start_date': '2023-01-01', 'employee_type': 'FT', 'cost_center': '90000001', 'department_number': '1', 'department_name': 'executive department'}}
prov_payload = {'birthrightAccess': [{'access_data': '99'}, {'access_data': '98'}, {'access_data': '97'}, {'access_data': '96'}, {'access_data': '95'}, {'access_data': '2'}], 'identity': {'identity_id': '3409d68329d7304a1d5b95658c405e62', 'create_ts': '2023-03-18 19:08:11.160', 'hr_id': '49', 'user_id': 'robert.m.hartman49', 'legal_first_name': 'robert', 'legal_middle_name': 'maurice', 'legal_last_name': 'hartman', 'preferred_first_name': 'robert', 'preferred_middle_name': 'maurice', 'preferred_last_name': 'hartman', 'use_preferred_name': 'false', 'job_title_code': 'eng', 'job_title_description': 'eng', 'job_title_level': '100', 'location_code': '1001', 'location_name': 'norfolk', 'email_work_primary': 'robert.hartman@hartmancorp.com', 'status': 'A', 'hire_start_date': '2023-01-01', 'employee_type': 'FT', 'cost_center': '90000001', 'department_number': '1', 'department_name': 'executive department'}}

def getAccessMeta(payload):
    platform_to_access_dict = {}
    if "birthrightAccess" in payload:
        for access in payload["birthrightAccess"]:
            piece_of_access = access["access_data"]
            platform = "1029012903912039" # TODO: lookup platform for each piece of access
            if platform in platform_to_access_dict:
                platform_to_access_dict[platform].append(piece_of_access)
            else:
                platform_to_access_dict[platform]= [piece_of_access]
        return platform_to_access_dict

def getAccountsForIdentity(platform_to_birthright_dict, payload):
    platform_to_account_dict = {}
    for key in platform_to_birthright_dict.keys():
        account = "m32l4jnkj2n34kbnk23n4" # TODO: lookup account for each platform, might be more than one, for the identity
        if key in platform_to_account_dict:
            platform_to_account_dict[key].append(account)
        else:
            platform_to_account_dict[key] = [account]
    return platform_to_account_dict

def getAccessForAccount(platform_to_account_dict):
    account_to_access_dict = {}
    tmp_access = ['98', '97', '19'] # TODO: take away after you build in lookup
    for key in platform_to_account_dict.keys():
        for account in platform_to_account_dict[key]:
            access = tmp_access # TODO: lookup access for each account that is birthright (need flag in snowflake)
            if account in account_to_access_dict:
                account_to_access_dict[account].append(access)
            else:
                account_to_access_dict[account] = access
    return account_to_access_dict

def calculateCurrentAccess(platform_to_account_dict, account_to_access_dict):
    current_birthright_access_dict = {}
    for platform, accounts in platform_to_account_dict.items():
        for account in accounts:
            if platform in current_birthright_access_dict:
                current_birthright_access_dict[platform].append({account: account_to_access_dict[account]})
            else:
                current_birthright_access_dict[platform] = [{account: account_to_access_dict[account]}]
    return current_birthright_access_dict

def calculateProvisioningPlan(current_birthright_access_dict, platform_to_birthright_dict):
    provision_access_dict = {}
    deprovision_access_dict = {}
    for platform, accounts in current_birthright_access_dict.items():
        for account in accounts:
            for account_key, access in account.items():
                birthright_for_platform = set(platform_to_birthright_dict[platform])
                current_birthright = set(access)
                birthright_to_add = birthright_for_platform.difference(current_birthright)
                birthright_to_remove = current_birthright.difference(birthright_for_platform)

                if platform in provision_access_dict:
                    provision_access_dict[platform].append({account_key: list(birthright_to_add)})
                elif platform not in provision_access_dict:
                    provision_access_dict[platform] = [{account_key: list(birthright_to_add)}]
                
                if platform in deprovision_access_dict:
                    deprovision_access_dict[platform].append({account_key: list(birthright_to_remove)})
                else:
                    deprovision_access_dict[platform] = [{account_key: list(birthright_to_remove)}]
    return provision_access_dict, deprovision_access_dict

def calculateDeprovisioningPlan(payload):
    if "birthrightAccess" not in payload:
        pass



platform_to_birthright_dict = getAccessMeta(prov_payload)
platform_to_account_dict = getAccountsForIdentity(platform_to_birthright_dict, prov_payload)
account_to_access_dict = getAccessForAccount(platform_to_account_dict)
current_birthright_access_dict = calculateCurrentAccess(platform_to_account_dict, account_to_access_dict)
provision_access_dict, deprovision_access_dict = calculateProvisioningPlan(current_birthright_access_dict, platform_to_birthright_dict)

print(provision_access_dict)
print(deprovision_access_dict)

# print(current_birthright_access_dict)