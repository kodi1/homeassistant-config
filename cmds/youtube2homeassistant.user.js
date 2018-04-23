// ==UserScript==
// @name         youtube to homeassistant
// @namespace    https://github.com/kodi1/homeassistant-config/raw/master/cmds/youtube2homeassistant.user.js
// @version      0.02
// @description  ha video
// @author       kodi1
// @compatible chrome
// @compatible firefox
// @compatible opera
// @compatible safari
// @include      http*://*.youtube.com/*
// @include      http*://youtube.com/*
// @include      http*://*.youtu.be/*
// @include      http*://youtu.be/*
// @run-at       document-end
// @require      https://openuserjs.org/src/libs/sizzle/GM_config.js
// @grant        GM_getValue
// @grant        GM_setValue
// @grant        GM_addStyle
// @grant        GM_xmlhttpRequest
// @grant        GM_registerMenuCommand
// @connect      *
// ==/UserScript==

//https://greasyfork.org/bg/scripts/33219-fastest-youtube-downloader-video-or-mp3

function go() {
    GM_config.init(
        {
            'id': 'HAConfig',
            'title': 'Home Assistant',
            'fields':
            {
                'server':
                {
                    'label': 'server',
                    'type': 'text',
                    'default': 'homeassistant server'
                },
                'player':
                {
                    'label': 'video player',
                    'type': 'text',
                    'default': 'kodi'
                },
                'player_audio':
                {
                    'label': 'audio player',
                    'type': 'text',
                    'default': 'cromecast'
                },
                'port':
                {
                    'label': 'port',
                    'type': 'unsigned int',
                    'default': '8123'
                },
                'pass':
                {
                    'label': 'pass',
                    'type': 'text',
                    'default': 'super secret password'
                },
            }
        });
    GM_registerMenuCommand('Configure HA', function () {GM_config.open();});
    start();
}

window.addEventListener('spfdone', go, false);
window.addEventListener('DOMContentLoaded', go, false);
window.addEventListener('yt-navigate-finish', go, false);

function start() {
    function isMaterial() {
        var temp;
        temp = document.querySelector("ytd-app, [src*='polymer'],link[href*='polymer']");
        if (!temp) { // old UI
            var urldl = window.location.href;
            if(str.indexOf("youdl") < 0){
                temp = document.createElement("template");
                temp.innerHTML = //
                    `<div id='material-notice' style='border-radius:2px;color:#FFF;padding:10px;background-color:#ff0000;box-shadow:0 0 3px rgba(0,0,0,.5);font-size:18px;position:fixed;bottom:20px;right:50px;z-index:99999'>
<strong><ins>WARNING : </ins></strong>youtube to homeassistant is <B>Only compatible with the new YouTube Material Layout</B><br>
<a href='https://youtube.com/new' target='_blank' style='font-weight:bold;'>Click here</a> to activate the new YouTube Material Layout.<br>
<br/><br/>
<span id='close' onclick='document.getElementById("material-notice").remove(); return false;' align='center' STYLE='display:block;width:100px;height: 100%;margin: 0 auto;'><strong><ins><a href=""> [X] CLOSE </a></ins></strong></span>
</div>`;
                document.documentElement.appendChild(temp.content.firstChild);
                document.documentElement.removeAttribute("data-user_settings");
                return true;
            }
        }
    }
    isMaterial();
    var lasturl = "";

    start_player = function(player_id) {
        var payload = "{\"entity_id\": \"media_player."+player_id+"\"}";
        var url = "http:\/\/"+GM_config.get('server')+":"+GM_config.get('port')+"\/api\/services\/media_player\/turn_on";
        var request_details = {
            method: "POST",
            url: url,
            data: payload,
            binary: true,
            headers: {
                "Content-Type": "application/json",
                "x-ha-access": GM_config.get('server')
            },
            onload: function(response) {
                console.log(response);
            }
        };

        console.log(payload);
        console.log(url);
        console.log(request_details);

        GM_xmlhttpRequest(request_details);
    };

    sent_data = function(player_id, content_id) {
        var payload = "{\"entity_id\": \"media_player."+player_id+"\",\"media_content_id\": \""+window.location.href+"\",\"media_content_type\": \""+content_id+"\"}";
        var url = "http:\/\/"+GM_config.get('server')+":"+GM_config.get('port')+"\/api\/services\/media_extractor\/play_media";
        var request_details = {
            method: "POST",
            url: url,
            data: payload,
            binary: true,
            headers: {
                "Content-Type": "application/json",
                "x-ha-access": GM_config.get('server')
            },
            onload: function(response) {
                console.log(response);
            }
        };

        console.log(payload);
        console.log(url);
        console.log(request_details);

        GM_xmlhttpRequest(request_details);
    };

    video_onclick = function() {
        document.getElementById("movie_player").stopVideo();
        start_player(GM_config.get('player'));
        setTimeout(sent_data(GM_config.get('player'), "video"), 1000);
    };

    audio_onclick = function() {
        document.getElementById("movie_player").stopVideo();
        sent_data(GM_config.get('player_audio'), "audio/mp3");
    };

    getSpan = function(text, className) {
        var _tn = document.createTextNode(text);
        var span = document.createElement("span");
        span.className = className;
        span.appendChild(_tn);
        return span;
    };

    createButton = function(id, cb_func) {
        var obj = document.querySelector('#top-level-buttons');
        if (obj !== null) {
            // check if the button has already been created
            var btnRow = document.getElementById(id);
            if (btnRow === null) {
                var bestvd2 = document.createElement("div");
                bestvd2.id = id;
                bestvd2.className = "style-scope";

                var bvd2_btn = document.createElement("div");
                bvd2_btn.className = "style-scope bvd2_btn";

                if (true === id.toLowerCase().includes("video")) {
                    bvd2_btn.style = "background-color: green; border: solid 2px green; border-radius: 2px; color: white; padding: 0px 15px; font-size: 14px; cursor:pointer; height:33px;margin-right: 7px;margin-top: 7px;line-height: 33px;font-weight: 500; display:inline-block;";
                } else {
                    bvd2_btn.style = "background-color: blue; border: solid 2px blue; border-radius: 2px; color: white; padding: 0px 15px; font-size: 14px; cursor:pointer; height:33px;margin-right: 7px;margin-top: 7px;line-height: 33px;font-weight: 500; display:inline-block;";
                }
                bvd2_btn.appendChild(getSpan(id, ""));
                bvd2_btn.onclick = cb_func;

                obj.parentNode.appendChild(bestvd2, obj);
                bestvd2.appendChild(bvd2_btn);
            }
        }
    };

    var intervalCheck = setInterval(function() {
        createButton('HA Video', video_onclick);
        createButton('HA Audio', audio_onclick);
    }, 1000);
}
