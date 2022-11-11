// WEB based SPD-500 serial program

// global port variable
var port = 0;
// price in integer to display
var intprice = 0;

// CRC16 generator
function crc16(data, offset = 0) {
    var crc, length;
    length = data.length;

    if (data === null || offset < 0 || offset > data.length - 1 && offset + length > data.length) {
      return 0;
    }
    crc = 0;
    for (var i = 0, _pj_a = length; i < _pj_a; i += 1) {
      crc ^= data[i];
  
      for (var j = 0, _pj_b = 8; j < _pj_b; j += 1) {
        if ((crc & 1) > 0) {
          crc = (crc >> 1) ^ 40961;
        } else {
          crc = crc >> 1;
        }
      }
    }
    return crc.toString(16);
  }

// connect device via WebSerial API 
async function connectDevice(){
    // usb vendor id required 
    const filter = {usbVendorId: 0x067B};
                    // {usbVendorId: 0x0403}];
    
    const connectButton = document.getElementById("connect");
    try {
        port = await navigator.serial.requestPort({ filters: [filter] });
        await port.open({
            baudRate: 115200
        })
    } catch (e) {
        // The prompt has been dismissed without selecting a device.
        alert("port not connected")
    }
    console.log(port.productName);
    console.log(port.manufacturerName);
}

// receive confirm protocol
async function sendConfirm(){
  const confirm = new Uint8Array([0x06,0x06,0x06,0x06]);
  const writer = port.writable.getWriter();
  await writer.write(confirm);
  writer.releaseLock();
}

// this loop must run before credit card is inserted
async function purchaseLoop(){
  // var sequence = 0;
    // console.log("loop")
    while (port.readable) {
        // console.log(`sequence ${sequence}`);
        const reader = port.readable.getReader();
        while (true) {
          let value, done;
          try {
            ({ value, done } = await reader.read());
          } catch (error) {
            alert("payment failed")
            break;
          }
          if (done) {
            break;
          }
          if (value.length > 0){
            // console.log(value)
            // when 'any' message runs in the loop immediatly returns [06, 06, 06, 06] 
            sendConfirm();
            if(value[6] == 0){
                alert(`credit card purchace approved : ${intprice} won`);
            }
            break
          }
        }
        // console.log("read done")
        // sequence++;
        reader.releaseLock();
      }

}  

// convert input price into protocol 
function getPrice(){
    // read price vale in won from input at click
    var price = document.getElementById('price').value;

    var zero = "0";
    var plength = price.length;
    intprice = price;

    // set price value to 6 digit value (ex. 1000 won --> 001000 / 2500 won --> 002500 )
    if(plength<6){
        for(var i = 0; 6-plength-i>0;i++){
            price = zero.concat(price);
        }
    }

    // packet structure refer to datasheet
    var STX = [0x02];
    var retcrc =[0x00, 0x08, 0xf8, 0x20, 0x02, parseInt(price.substring(0,2),16), parseInt(price.substring(2,4),16), parseInt(price.substring(4,6),16), 0x03];
    var pricecrc = crc16(retcrc);
    var clength = pricecrc.length;
    
    // set crc value to hex 4 digits
    if(clength<4){
        for(var i = 0; 4-clength-i>0;i++){
            pricecrc = zero.concat(pricecrc);
        }
    }

    // divide CRC value to CRC_H, CRC_L
    var fincrc = [parseInt(pricecrc.substring(0,2),16), parseInt(pricecrc.substring(2,4),16)];

    // reconfigure packet to send in format
    var price_protocol = STX.concat(retcrc.concat(fincrc));
    price_protocol = new Uint8Array(price_protocol);

    return price_protocol;
}

// send price to SPD500
async function sendPrice(){
    price_protocol = getPrice();
    const writer = port.writable.getWriter();
    await writer.write(price_protocol);
    writer.releaseLock();
}

// close serial port
async function portClose(){
    await port.close();
    document.write("close");
}
