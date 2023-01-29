document.getElementById("save").addEventListener("click", saveAlert);

function saveAlert(){          
    chrome.storage.sync.set({'script': $('#quote').val(), 'condition' : $('#conditions').val(), 'condition_price' : $('#price_condition').val()});
    
}