# D-Edge Task

## Python Bandcamp scraper
*My comments during the task:*  
- There are WEB and Mobile APIs. We can scrape both but there are some obstacles.
- Web app has CAPTCHA which needs to be resolved to get cookies (easier)
- Mobile API has one hashed value in headers which I cannot recreate for this task (need more time) or we can get access token by logging in to mobile app (appium). This is possible but I would need more time. (more elegant solution)

*Conclusion:*  
- I will implement web API scraper since I have limited time for this task. 
- I analyzed how website works and I decided to use anti-captcha instead of proxies. (Proxies can work as well)
  - https://anti-captcha.com/

## *Idea*
1. Use selenium to log in with credentials in browser
2. Take cookies from response headers and use it for API requests
3. Get fan id from html and use it in payload
4. Collect wishlist, artists, genres and collection using API calls
5. Each scraped item is one record with different types (wishlist, artists, genres and collection)
6. Calculate and print reliability when all data are collected. (I just logged out the percentage since it doesn't have the same format as other items in output file)

API links (settings file):

     https://bandcamp.com/api/fancollection/1/wishlist_items
     https://bandcamp.com/api/fancollection/1/collection_items
     https://bandcamp.com/api/fancollection/1/following_bands
     https://bandcamp.com/api/fancollection/1/following_genres

**Payload**:
```json
{
      "fan_id": <fan_id>,                # fan_id we get from page when we log in
      "older_than_token": <timestamp>,
      "count": 99                        # 99 is maximum in 1 request
}
```

**Output**:
- Each item from wishlist/collection/genres/artists has *type* and *data* fields. 
```json
{"type": "genres", "data": {"discover_id": 166, "name": "World", "norm_name": "world", "token": "world", "is_following": true, "date": null, "genre_id": 26, "tag_id": 0, "geoname_id": 0, "format_type": "all", "art_ids": [2461845631, 2017712773, 2899301307, 1747601374], "location": null, "discover_url": null, "tag_page_url": "http://bandcamp.com/tag/world", "display_name": "world"}},
{"type": "wishlist", "data": {"fan_id": 9559639, "item_id": 4216501319, "item_type": "album", "band_id": 1041046483, "added": "10 May 2023 08:44:38 GMT", "updated": "10 May 2023 08:44:38 GMT", "purchased": null, "sale_item_id": null, "sale_item_type": null, "tralbum_id": 4216501319, "tralbum_type": "a", "featured_track": 4217068776, "why": null, "hidden": null, "index": null, "also_collected_count": 83, "url_hints": {"subdomain": "dudal", "custom_domain": null, "custom_domain_verified": null, "slug": "santeboutique", "item_type": "a"}, "item_title": "santeboutique", "item_url": "https://dudal.bandcamp.com/album/santeboutique", "item_art_id": 394874881, "item_art_url": "https://f4.bcbits.com/img/a0394874881_9.jpg", "item_art": {"url": "https://f4.bcbits.com/img/a0394874881_9.jpg", "thumb_url": "https://f4.bcbits.com/img/a0394874881_3.jpg", "art_id": 394874881}, "band_name": "dudal", "band_url": "https://dudal.bandcamp.com", "genre_id": 3, "featured_track_title": "moustache blanche", "featured_track_number": 1, "featured_track_is_custom": false, "featured_track_duration": 54.0, "featured_track_url": null, "featured_track_encodings_id": 3442184974, "package_details": null, "num_streamable_tracks": 9, "is_purchasable": true, "is_private": false, "is_preorder": false, "is_giftable": true, "is_subscriber_only": false, "is_subscription_item": false, "service_name": null, "service_url_fragment": null, "gift_sender_name": null, "gift_sender_note": null, "gift_id": null, "gift_recipient_name": null, "album_id": 4216501319, "album_title": "santeboutique", "listen_in_app_url": null, "band_location": null, "band_image_id": null, "release_count": null, "message_count": null, "is_set_price": false, "price": 0.0, "has_digital_download": null, "merch_ids": [2820342154], "merch_sold_out": false, "currency": "EUR", "label": null, "label_id": null, "require_email": null, "item_art_ids": null, "releases": null, "discount": null, "token": "1683708278:4216501319:a::", "variant_id": null, "merch_snapshot": null, "featured_track_license_id": null, "licensed_item": null, "download_available": true}},
{"type": "astists", "data": {"band_id": 599671952, "image_id": 25847747, "art_id": 1252756235, "url_hints": {"subdomain": "arovane", "custom_domain": null}, "name": "arovane", "is_following": true, "is_subscribed": null, "location": "Germany", "date_followed": "25 Apr 2023 13:56:32 GMT", "token": "1682430992:599671952"}},
{"type": "collection", "data": {"fan_id": 9559639, "item_id": 2728663825, "item_type": "album", "band_id": 2797382021, "added": "29 Apr 2023 20:01:08 GMT", "updated": "29 Apr 2023 20:01:08 GMT", "purchased": "29 Apr 2023 20:01:08 GMT", "sale_item_id": 242585381, "sale_item_type": "p", "tralbum_id": 2728663825, "tralbum_type": "a", "featured_track": 3382834261, "why": null, "hidden": null, "index": null, "also_collected_count": 861, "url_hints": {"subdomain": "glitchblack", "custom_domain": null, "custom_domain_verified": null, "slug": "interdimensional", "item_type": "a"}, "item_title": "Interdimensional", "item_url": "https://glitchblack.bandcamp.com/album/interdimensional", "item_art_id": 3037883461, "item_art_url": "https://f4.bcbits.com/img/a3037883461_9.jpg", "item_art": {"url": "https://f4.bcbits.com/img/a3037883461_9.jpg", "thumb_url": "https://f4.bcbits.com/img/a3037883461_3.jpg", "art_id": 3037883461}, "band_name": "Glitch Black", "band_url": "https://glitchblack.bandcamp.com", "genre_id": 10, "featured_track_title": "Damage Control", "featured_track_number": 1, "featured_track_is_custom": false, "featured_track_duration": 200.306, "featured_track_url": null, "featured_track_encodings_id": 1877304194, "package_details": null, "num_streamable_tracks": 16, "is_purchasable": true, "is_private": false, "is_preorder": false, "is_giftable": true, "is_subscriber_only": false, "is_subscription_item": false, "service_name": null, "service_url_fragment": null, "gift_sender_name": null, "gift_sender_note": null, "gift_id": null, "gift_recipient_name": null, "album_id": 2728663825, "album_title": "Interdimensional", "listen_in_app_url": "https://bandcamp.com/redirect_to_app?fallback_url=https%3A%2F%2Fbandcamp.com%2Fthis_is_an_appstore_url%3Fapp%3Dfan_app&url=x-bandcamp%3A%2F%2Fshow_tralbum%3Ftralbum_type%3Da%26tralbum_id%3D2728663825%26play%3D1&sig=4b63e86e66faf51a28f7c981e058fb06", "band_location": null, "band_image_id": null, "release_count": null, "message_count": null, "is_set_price": false, "price": 0.0, "has_digital_download": null, "merch_ids": null, "merch_sold_out": null, "currency": "USD", "label": null, "label_id": null, "require_email": null, "item_art_ids": null, "releases": null, "discount": null, "token": "1682798468:2728663825:a::", "variant_id": null, "merch_snapshot": null, "featured_track_license_id": null, "licensed_item": null, "download_available": true}}
```

### RUN:

1.     docker build -t bandcamp .
2.     docker run bandcamp


## **BONUS*:
- I would like to explain my idea with mobile API.

### *Request to get access_token:*
```
POST https://bandcamp.com/oauth_login
```
Headers:
```json
  { 
      "cookie": "client_id=5DC17BCE9A424FEDCD22E33B274DB19CC6F89FB390A2F3AFF943781E5CCCD38D",                                                                      
      "cookie": "BACKENDID3=flexocentral-drtv-6",                                                                                                                    
      "cookie": "BACKENDID=flexo1central-j378-4",                                                                                                                    
      "accept": "*/*",                                                                                                                                               
      "content-type": "application/x-www-form-urlencoded",                                                                                                                 
      "x-bandcamp-dm": "784a9c3decd63b7a9a102ab8eddcf2c67ceeed83",                                                                                                          
      "user-agent": "Bandcamp/219847 CFNetwork/1399 Darwin/22.1.0",                                                                                                     
      "accept-language": "en-GB,en;q=0.9",                                                                                                                                   
      "content-length": "166",                                                                                                                                               
      "accept-encoding": "gzip, deflate, br"
  }
```
URLEncoded form:
```json                                                                                                                   
  {
      "grant_type": "password", 
      "username": <username>, 
      "password": <password>, 
      "username_is_user_id": "1", 
      "client_id": "133", 
      "client_secret": "CVmGPEtGmkd9gpC/fZXhKbMhkIk2L4SLWbi92+nlwhk="
  }
```
Response:
```json
  {
      "access_token": "3978469224.133.1683579867.lFabO2U7xYQ61h6KQ7BHgpaFP68=",
      "expires_in": 3600,
      "ok": true,
      "refresh_token": "14435927.0.TGi5PFt5Ts2qWeQm84iH7PxJC2U=",
      "token_type": "bearer"
  }
```
Unfortunately I cannot recreate **x-bandcamp-dm** value in headers. All other fields are available. 

Idea is to use Appium to login in like with Selenium just to get access_token and use it for authorization field. Once we have access_token we can get refresh token. It expires in 1 hour.

#### Mobile API for wishlist:
```
GET https://bandcamp.com/api/collectionsync/1/wishlist?page_size=200&offset=1:1683064412:2955047868:a
```
Headers:
```json
  { 
      "cookie": "client_id=5DC17BCE9A424FEDCD22E33B274DB19CC6F89FB390A2F3AFF943781E5CCCD38D",                                                                      
      "cookie": "BACKENDID3=flexocentral-drtv-6",                                                                                                                   
      "cookie": "BACKENDID=flexo1central-j378-4",                                                                                                                   
      "accept": "*/*",                                                                                                                                              
      "accept-encoding": "gzip, deflate, br",                                                                                                                               
      "user-agent": "Bandcamp/219847 CFNetwork/1399 Darwin/22.1.0",                                                                                                     
      "authorization": "Bearer 3978469224.133.1683579867.lFabO2U7xYQ61h6KQ7BHgpaFP68=",     # current obstacle                                                                               
      "accept-language": "en-GB,en;q=0.9" 
  }
```

### !!! *Things I didn't do*:
- I didn't hide credentials and API key. Sorry.