

window.onload= function(){
    var oV = document.getElementById('player');
    var aInput = document.getElementsByTagName('input');

    var timer = null;
    aInput[0].onclick = function(){
        if( oV.paused ){//如果是暂停的
            oV.play();
            this.value = '暂停';
            nowTime();
            timer =setInterval(nowTime,1000);
        }
        else{
            oV.pause();
            this.value = '播放';
            clearInterval(timer);
        }
    };

    aInput[2].value = oV.duration;

    aInput[3].onclick = function(){
        if( oV.muted ){
            oV.volume = 1;
            this.value = '静音';
            oV.muted = false;
        }
        else{
            oV.volume = 0;
            this.value = '取消静音';
            oV.muted = true;
        }
    };

    
    function nowTime(){
        aInput[1].value =oV.currentTime
      }
    }