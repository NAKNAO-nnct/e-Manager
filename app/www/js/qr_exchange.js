function startReadQR(video, callback, error){
  var store = {
      all_length: 0,
      length: 0
  };

  var state = "run";

  qrcode.callback = function(res) {
    if(res == 'error decoding QR Code'){
      error();
    } else {
      console.log("read", res);
      receiveQr(res, store, callback);
    }
  }
  var videoRead = function() {
    var w = video.videoWidth;
    var h = video.videoHeight;
    var canvas = document.createElement("canvas");
    canvas.width = w;
    canvas.height = h;
    var ctx = canvas.getContext("2d");

    var draw = function(){
      if(state == "stop"){
        return;
      }

      requestAnimationFrame(draw);
      ctx.drawImage(video, 0, 0, w, h);
      var img = canvas.toDataURL("image/png");
      qrcode.decode(img);
    };

    draw();
  }

  if (video.readyState == 0) {
    video.onloadedmetadata = videoRead;
  } else {
    videoRead();
  }

  return function(){
    state = "stop";
  };
}
