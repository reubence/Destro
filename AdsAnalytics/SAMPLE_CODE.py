# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.api import FacebookAdsApi

access_token = 'EAAGdnbY3picBAJZCHnsHTZBTitLD7hebTpoAvhZBt6ZBPZAuJulyvZCwifUsEe2rji44gJhWifViAK0tEUA1qIle0B1YuIFWOzHfscljYIKh0SijlITzoa8kBK5OAyYmhtXsmi6VOchAbQ6gcckzhVy35gqbN0NZBRXEF50cWpZAebtKYLZA7mmEfG7sZCu0NqeJMZD'
ad_account_id = 'act_1131932527250773'
app_secret = 'a0c66a0a833c5195d624975d0a9060b3'
app_id = '454775669237287'
FacebookAdsApi.init(access_token=access_token)

fields = [
    'results',
    'result_rate',
    'reach',
    'frequency',
    'impressions',
    'delivery',
    'spend',
    'impressions_gross',
    'impressions_auto_refresh',
    'attribution_setting',
    'quality_score_organic',
    'quality_score_ectr',
    'quality_score_ecvr',
    'cost_per_result',
    'cpp',
    'cpm',
    'actions:page_engagement',
    'actions:like',
    'actions:comment',
    'actions:post_engagement',
    'actions:post_reaction',
    'actions:onsite_conversion_post_save',
    'actions:post',
    'actions:photo_view',
    'actions:rsvp',
    'actions:checkin',
    'actions:full_view',
    'unique_actions:full_view',
    'ar_effect_share:ar_effect_share',
    'cost_per_action_type:page_engagement',
    'cost_per_action_type:like',
    'cost_per_action_type:post_engagement',
    'cost_per_action_type:rsvp',
    'unique_video_continuous_2_sec_watched_actions:video_view',
    'video_continuous_2_sec_watched_actions:video_view',
    'actions:video_view',
    'video_thruplay_watched_actions:video_view',
    'video_p25_watched_actions:video_view',
    'video_p50_watched_actions:video_view',
    'video_p75_watched_actions:video_view',
    'video_p95_watched_actions:video_view',
    'video_p100_watched_actions:video_view',
    'video_avg_time_watched_actions:video_view',
    'video_play_actions:video_view',
    'canvas_avg_view_time',
    'canvas_avg_view_percent',
    'cost_per_2_sec_continuous_video_view:video_view',
    'cost_per_action_type:video_view',
    'cost_per_thruplay:video_view',
    'actions:click_to_call_call_confirm',
    'actions:link_click',
    'unique_actions:link_click',
    'outbound_clicks:outbound_click',
    'unique_outbound_clicks:outbound_click',
    'website_ctr:link_click',
    'unique_link_clicks_ctr',
    'outbound_clicks_ctr:outbound_click',
    'unique_outbound_clicks_ctr:outbound_click',
    'clicks',
    'unique_clicks',
    'ctr',
    'unique_ctr',
    'cost_per_action_type:link_click',
    'cost_per_unique_action_type:link_click',
    'cost_per_outbound_click:outbound_click',
    'cost_per_unique_outbound_click:outbound_click',
    'cpc',
    'cost_per_unique_click',
    'estimated_ad_recallers',
    'estimated_ad_recall_rate',
    'cost_per_estimated_ad_recallers',
    'actions:omni_achievement_unlocked',
    'cost_per_action_type:omni_achievement_unlocked',
    'action_values:omni_achievement_unlocked',
    'unique_actions:omni_achievement_unlocked',
    'cost_per_unique_action_type:omni_achievement_unlocked',
    'actions:add_payment_info',
    'cost_per_action_type:add_payment_info',
    'action_values:add_payment_info',
    'unique_actions:add_payment_info',
    'cost_per_unique_action_type:add_payment_info',
    'actions:omni_add_to_cart',
    'cost_per_action_type:omni_add_to_cart',
    'action_values:omni_add_to_cart',
    'unique_actions:omni_add_to_cart',
    'cost_per_unique_action_type:omni_add_to_cart',
    'actions:add_to_wishlist',
    'cost_per_action_type:add_to_wishlist',
    'action_values:add_to_wishlist',
    'unique_actions:add_to_wishlist',
    'cost_per_unique_action_type:add_to_wishlist',
    'actions:omni_activate_app',
    'cost_per_action_type:omni_activate_app',
    'action_values:omni_activate_app',
    'unique_actions:omni_activate_app',
    'cost_per_unique_action_type:omni_activate_app',
    'actions:omni_app_install',
    'cost_per_action_type:omni_app_install',
    'conversions:submit_application_total',
    'cost_per_conversion:submit_application_total',
    'conversion_values:submit_application_total',
    'conversions:schedule_total',
    'cost_per_conversion:schedule_total',
    'conversion_values:schedule_total',
    'actions:omni_initiated_checkout',
    'cost_per_action_type:omni_initiated_checkout',
    'action_values:omni_initiated_checkout',
    'unique_actions:omni_initiated_checkout',
    'cost_per_unique_action_type:omni_initiated_checkout',
    'conversions:contact_total',
    'cost_per_conversion:contact_total',
    'conversion_values:contact_total',
    'actions:omni_view_content',
    'cost_per_action_type:omni_view_content',
    'action_values:omni_view_content',
    'unique_actions:omni_view_content',
    'cost_per_unique_action_type:omni_view_content',
    'actions:omni_spend_credits',
    'cost_per_action_type:omni_spend_credits',
    'action_values:omni_spend_credits',
    'unique_actions:omni_spend_credits',
    'cost_per_unique_action_type:omni_spend_credits',
    'actions:omni_custom',
    'cost_per_action_type:omni_custom',
    'actions:app_engagement',
    'cost_per_action_type:app_engagement',
    'actions:app_story',
    'cost_per_action_type:app_story',
    'actions:app_use',
    'cost_per_action_type:app_use',
    'conversions:donate_total',
    'cost_per_conversion:donate_total',
    'conversion_values:donate_total',
    'actions:games_plays',
    'cost_per_action_type:games_plays',
    'actions:onsite_conversion_find_location',
    'conversions:ad_click_mobile_app',
    'cost_per_conversion:ad_click_mobile_app',
    'conversions:ad_impression_mobile_app',
    'cost_per_conversion:ad_impression_mobile_app',
    'actions:landing_page_view',
    'cost_per_action_type:landing_page_view',
    'unique_actions:landing_page_view',
    'cost_per_unique_action_type:landing_page_view',
    'actions:lead',
    'cost_per_action_type:lead',
    'action_values:lead',
    'actions:omni_level_achieved',
    'cost_per_action_type:omni_level_achieved',
    'action_values:omni_level_achieved',
    'unique_actions:omni_level_achieved',
    'cost_per_unique_action_type:omni_level_achieved',
    'conversions:find_location_total',
    'cost_per_conversion:find_location_total',
    'conversion_values:find_location_total',
    'actions:app_custom_event_fb_mobile_d2_retention',
    'cost_per_action_type:app_custom_event_fb_mobile_d2_retention',
    'unique_actions:app_custom_event_fb_mobile_d2_retention',
    'cost_per_unique_action_type:app_custom_event_fb_mobile_d2_retention',
    'actions:app_custom_event_fb_mobile_d7_retention',
    'cost_per_action_type:app_custom_event_fb_mobile_d7_retention',
    'unique_actions:app_custom_event_fb_mobile_d7_retention',
    'cost_per_unique_action_type:app_custom_event_fb_mobile_d7_retention',
    'actions:offline_conversion_other',
    'cost_per_action_type:offline_conversion_other',
    'action_values:offline_conversion_other',
    'actions:onsite_conversion_flow_complete',
    'cost_per_action_type:onsite_conversion_flow_complete',
    'action_values:onsite_conversion_flow_complete',
    'actions:onsite_conversion_click_to_call',
    'conversions:customize_product_total',
    'cost_per_conversion:customize_product_total',
    'conversion_values:customize_product_total',
    'purchase_roas:omni_purchase',
    'actions:omni_purchase',
    'cost_per_action_type:omni_purchase',
    'action_values:omni_purchase',
    'unique_actions:omni_purchase',
    'cost_per_unique_action_type:omni_purchase',
    'actions:omni_rate',
    'cost_per_action_type:omni_rate',
    'action_values:omni_rate',
    'unique_actions:omni_rate',
    'cost_per_unique_action_type:omni_rate',
    'actions:omni_complete_registration',
    'cost_per_action_type:omni_complete_registration',
    'action_values:omni_complete_registration',
    'unique_actions:omni_complete_registration',
    'cost_per_unique_action_type:omni_complete_registration',
    'actions:omni_search',
    'cost_per_action_type:omni_search',
    'action_values:omni_search',
    'unique_actions:omni_search',
    'cost_per_unique_action_type:omni_search',
    'store_visit_actions:store_visit',
    'cost_per_store_visit_action:store_visit',
    'conversions:subscribe_total',
    'cost_per_conversion:subscribe_total',
    'conversion_values:subscribe_total',
    'conversions:start_trial_total',
    'cost_per_conversion:start_trial_total',
    'conversion_values:start_trial_total',
    'actions:omni_tutorial_completion',
    'cost_per_action_type:omni_tutorial_completion',
    'action_values:omni_tutorial_completion',
    'unique_actions:omni_tutorial_completion',
    'cost_per_unique_action_type:omni_tutorial_completion',
    'actions:app_custom_event_fb_mobile_achievement_unlocked',
    'action_values:app_custom_event_fb_mobile_achievement_unlocked',
    'unique_actions:app_custom_event_fb_mobile_achievement_unlocked',
    'actions:app_custom_event_fb_mobile_add_payment_info',
    'actions:offsite_conversion_fb_pixel_add_payment_info',
    'actions:offline_conversion_add_payment_info',
    'action_values:app_custom_event_fb_mobile_add_payment_info',
    'action_values:offsite_conversion_fb_pixel_add_payment_info',
    'action_values:offline_conversion_add_payment_info',
    'unique_actions:app_custom_event_fb_mobile_add_payment_info',
    'actions:app_custom_event_fb_mobile_add_to_cart',
    'actions:offsite_conversion_fb_pixel_add_to_cart',
    'actions:offline_conversion_add_to_cart',
    'actions:onsite_conversion_add_to_cart',
    'action_values:app_custom_event_fb_mobile_add_to_cart',
    'action_values:offsite_conversion_fb_pixel_add_to_cart',
    'action_values:offline_conversion_add_to_cart',
    'unique_actions:app_custom_event_fb_mobile_add_to_cart',
    'actions:app_custom_event_fb_mobile_add_to_wishlist',
    'actions:offsite_conversion_fb_pixel_add_to_wishlist',
    'actions:offline_conversion_add_to_wishlist',
    'action_values:app_custom_event_fb_mobile_add_to_wishlist',
    'action_values:offsite_conversion_fb_pixel_add_to_wishlist',
    'action_values:offline_conversion_add_to_wishlist',
    'unique_actions:app_custom_event_fb_mobile_add_to_wishlist',
    'actions:app_custom_event_fb_mobile_activate_app',
    'action_values:app_custom_event_fb_mobile_activate_app',
    'unique_actions:app_custom_event_fb_mobile_activate_app',
    'actions:mobile_app_install',
    'actions:app_install',
    'conversions:submit_application_mobile_app',
    'conversions:submit_application_website',
    'conversions:submit_application_offline',
    'conversion_values:submit_application_mobile_app',
    'conversion_values:submit_application_website',
    'conversion_values:submit_application_offline',
    'conversions:schedule_mobile_app',
    'conversions:schedule_website',
    'conversions:schedule_offline',
    'conversion_values:schedule_mobile_app',
    'conversion_values:schedule_website',
    'conversion_values:schedule_offline',
    'actions:app_custom_event_fb_mobile_initiated_checkout',
    'actions:offsite_conversion_fb_pixel_initiate_checkout',
    'actions:offline_conversion_initiate_checkout',
    'action_values:app_custom_event_fb_mobile_initiated_checkout',
    'action_values:offsite_conversion_fb_pixel_initiate_checkout',
    'action_values:offline_conversion_initiate_checkout',
    'unique_actions:app_custom_event_fb_mobile_initiated_checkout',
    'conversions:contact_mobile_app',
    'conversions:contact_website',
    'conversions:contact_offline',
    'conversion_values:contact_mobile_app',
    'conversion_values:contact_website',
    'conversion_values:contact_offline',
    'actions:app_custom_event_fb_mobile_content_view',
    'actions:offsite_conversion_fb_pixel_view_content',
    'actions:offline_conversion_view_content',
    'actions:onsite_conversion_view_content',
    'action_values:app_custom_event_fb_mobile_content_view',
    'action_values:offsite_conversion_fb_pixel_view_content',
    'action_values:offline_conversion_view_content',
    'unique_actions:app_custom_event_fb_mobile_content_view',
    'actions:app_custom_event_fb_mobile_spent_credits',
    'actions:credit_spent',
    'action_values:app_custom_event_fb_mobile_spent_credits',
    'action_values:credit_spent',
    'unique_actions:app_custom_event_fb_mobile_spent_credits',
    'cost_per_unique_action_type:app_custom_event_fb_mobile_spent_credits',
    'actions:app_custom_event_other',
    'conversions:donate_mobile_app',
    'conversions:donate_website',
    'conversions:donate_offline',
    'conversion_values:donate_mobile_app',
    'conversion_values:donate_website',
    'conversion_values:donate_offline',
    'actions:offsite_conversion_fb_pixel_lead',
    'actions:offline_conversion_lead',
    'actions:onsite_conversion_lead_grouped',
    'action_values:offsite_conversion_fb_pixel_lead',
    'action_values:offline_conversion_lead',
    'action_values:onsite_conversion_lead_grouped',
    'actions:app_custom_event_fb_mobile_level_achieved',
    'action_values:app_custom_event_fb_mobile_level_achieved',
    'unique_actions:app_custom_event_fb_mobile_level_achieved',
    'conversions:find_location_mobile_app',
    'conversions:find_location_website',
    'conversions:find_location_offline',
    'conversion_values:find_location_mobile_app',
    'conversion_values:find_location_website',
    'conversion_values:find_location_offline',
    'conversions:customize_product_mobile_app',
    'conversions:customize_product_website',
    'conversions:customize_product_offline',
    'conversion_values:customize_product_mobile_app',
    'conversion_values:customize_product_website',
    'conversion_values:customize_product_offline',
    'website_purchase_roas:offsite_conversion_fb_pixel_purchase',
    'mobile_app_purchase_roas:app_custom_event_fb_mobile_purchase',
    'actions:app_custom_event_fb_mobile_purchase',
    'actions:offsite_conversion_fb_pixel_purchase',
    'actions:offline_conversion_purchase',
    'actions:onsite_conversion_purchase',
    'action_values:app_custom_event_fb_mobile_purchase',
    'action_values:offsite_conversion_fb_pixel_purchase',
    'action_values:offline_conversion_purchase',
    'action_values:onsite_conversion_purchase',
    'unique_actions:app_custom_event_fb_mobile_purchase',
    'actions:app_custom_event_fb_mobile_rate',
    'action_values:app_custom_event_fb_mobile_rate',
    'unique_actions:app_custom_event_fb_mobile_rate',
    'actions:app_custom_event_fb_mobile_complete_registration',
    'actions:offsite_conversion_fb_pixel_complete_registration',
    'actions:offline_conversion_complete_registration',
    'action_values:app_custom_event_fb_mobile_complete_registration',
    'action_values:offsite_conversion_fb_pixel_complete_registration',
    'action_values:offline_conversion_complete_registration',
    'unique_actions:app_custom_event_fb_mobile_complete_registration',
    'actions:app_custom_event_fb_mobile_search',
    'actions:offsite_conversion_fb_pixel_search',
    'actions:offline_conversion_search',
    'action_values:app_custom_event_fb_mobile_search',
    'action_values:offsite_conversion_fb_pixel_search',
    'action_values:offline_conversion_search',
    'unique_actions:app_custom_event_fb_mobile_search',
    'conversions:subscribe_mobile_app',
    'conversions:subscribe_website',
    'conversions:subscribe_offline',
    'conversion_values:subscribe_mobile_app',
    'conversion_values:subscribe_website',
    'conversion_values:subscribe_offline',
    'conversions:start_trial_mobile_app',
    'conversions:start_trial_website',
    'conversions:start_trial_offline',
    'conversion_values:start_trial_mobile_app',
    'conversion_values:start_trial_website',
    'conversion_values:start_trial_offline',
    'actions:app_custom_event_fb_mobile_tutorial_completion',
    'action_values:app_custom_event_fb_mobile_tutorial_completion',
    'unique_actions:app_custom_event_fb_mobile_tutorial_completion',
    'date_start',
    'date_stop',
    'account_id',
    'account_name',
    'campaign_group_name',
    'campaign_group_id',
    'campaign_name',
    'campaign_id',
    'adgroup_id',
    'adgroup_name',
    'objective',
    'buying_type',
    'start_time',
    'stop_time',
    'bid',
    'budget',
    'schedule',
]
params = {
    'time_range': {'since':'2021-01-03','until':'2021-03-01'},
    'filtering': [],
    'level': 'ad',
    'breakdowns': ['publisher_platform','impression_device'],
}
print(AdAccount(ad_account_id).get_insights(
    fields=fields,
    params=params,
))


