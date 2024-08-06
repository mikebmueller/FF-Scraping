
# Paste your cookie string here
cookie_string = "curl "https://fantasy.nfl.com/league/2586569/history/2022/standings?historyStandingsType=regular" ^
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" ^
  -H "Accept-Language: en-US,en;q=0.9" ^
  -H "Connection: keep-alive" ^
  -H ^"Cookie: gig_canary=true; gig_canary_ver=16174-3-28716225; at_check=true; AMCVS_F75C3025512D2C1D0A490D44^%^40AdobeOrg=1; gig_bootstrap_3_WPLZFkJ278FjSau2FfLCrTRUyksAjeYpcva-qIfGl71F4VWrI-7Xb5y0snqKXDva=auth-id_ver4; mp_b0295127740fa6adee7c1e57995a2073_mixpanel=^%^7B^%^22distinct_id^%^22^%^3A^%^20^%^22^%^24device^%^3A191294508f0900-0f2070dc0036ab-26001e51-1fa400-191294508f1900^%^22^%^2C^%^22^%^24device_id^%^22^%^3A^%^20^%^22191294508f0900-0f2070dc0036ab-26001e51-1fa400-191294508f1900^%^22^%^2C^%^22^%^24initial_referrer^%^22^%^3A^%^20^%^22https^%^3A^%^2F^%^2Ffantasy.nfl.com^%^2F^%^22^%^2C^%^22^%^24initial_referring_domain^%^22^%^3A^%^20^%^22fantasy.nfl.com^%^22^%^7D; gig_bootstrap_3_3g_DApOD0TCeN6ZJpzQMr7H1cIbtqtHwDjKVESN3N5oohMleIozT0I9WecPZeytT=auth-id_ver4; gig_canary=true; glt_3_3g_DApOD0TCeN6ZJpzQMr7H1cIbtqtHwDjKVESN3N5oohMleIozT0I9WecPZeytT=st2.s.AtLt8fk4gA.oxFvjtwfvbJDLE9AEe9Nk14QLb42v06RzzRLHjma5mfIFFGJtT1f9f8yDbh3TxNwF3UAZnk_fkLXN-CNwHVjhIJ-gwqHz9PxGpmjuI20HVmS4u_2Xac7MVcqXmfrt47T.d1g5mOhrtVmqkwS63w3iSACew1L_DejQj9HGamf6RFJGTIwdv1cT8nh6fiAyg0tdazvTvIYePVY9rgecvO_VQA.sc3; nflcs.prod.keyStoreDomainSyncList=id.nfl.com; nfl_web_sdk_plugin_storage=^%^2CpercentPageViewed^|lastRecPage^|nfl^%^20fantasy:unknown:unknown:consent^|string^%^2CpercentPageViewed^|percentPageViewed^|100^|number^%^2CpercentPageViewed^|initialPageViewed^|100^|number^%^2CpercentPageViewed^|maxPageViewed^|626^|number; glt_3_WPLZFkJ278FjSau2FfLCrTRUyksAjeYpcva-qIfGl71F4VWrI-7Xb5y0snqKXDva=st2.s.AtLt8fk4gA.oxFvjtwfvbJDLE9AEe9Nk14QLb42v06RzzRLHjma5mfIFFGJtT1f9f8yDbh3TxNwF3UAZnk_fkLXN-CNwHVjhIJ-gwqHz9PxGpmjuI20HVmS4u_2Xac7MVcqXmfrt47T.d1g5mOhrtVmqkwS63w3iSACew1L_DejQj9HGamf6RFJGTIwdv1cT8nh6fiAyg0tdazvTvIYePVY9rgecvO_VQA.sc3; AMCV_F75C3025512D2C1D0A490D44^%^40AdobeOrg=179643557^%^7CMCIDTS^%^7C19942^%^7CMCMID^%^7C43127222539628575784511226439704896898^%^7CMCAID^%^7CNONE^%^7CMCOPTOUT-1722981587s^%^7CNONE^%^7CvVersion^%^7C5.5.0; mbox=session^#64d9f38131f5415eb10faa97f2282ab8^#1722976248^|PC^#64d9f38131f5415eb10faa97f2282ab8.34_0^#1786219188; ff=uid^%^3D85fe50d78ee4268e91ae59559a07e380^%^26fu^%^3D13995736^%^26tz^%^3DUS^%^2FEastern^%^26env^%^3Dproduction^%^26g^%^3D102024^%^7CL^%^402586569~FinalFantasyFootball~11~end^%^20of^%^20an^%^20error^%^26d^%^3D1722974390^%^26h^%^3Dbc9c11adb0eb2274576011c25929584c^" ^
  -H "Sec-Fetch-Dest: document" ^
  -H "Sec-Fetch-Mode: navigate" ^
  -H "Sec-Fetch-Site: cross-site" ^
  -H "Upgrade-Insecure-Requests: 1" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36" ^
  -H ^"sec-ch-ua: ^\^"Not)A;Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"127^\^", ^\^"Chromium^\^";v=^\^"127^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^""

# Dict to store cookies
cookies = {}

# Loop through each cookie
for cookie in cookie_string.split('; '):
    # Split cookie into name and value
    cookie_parts = cookie.split('=')
    cookies[cookie_parts[0]] = cookie_parts[1]
