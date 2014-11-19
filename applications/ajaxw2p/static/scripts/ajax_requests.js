function get2GDenominations(callback)
{
    var _recv2gDenominations = function(r) {
        console.log(r)
        res = JSON.parse(r)
        if (res.status == 200) {
            denominations2G = res.denominations2G; 
            console.log('2gDenominations: ', denominations2G);
            callback(denominations2G)
        } else {
            console.log(res.error)
        }
    }

    ajax('ajax/plans/2g', null, _recv2gDenominations)
}

function get3GDenominations(callback)
{
    var _recv3gDenominations = function(r) {
        console.log(r)
        res = JSON.parse(r)
        if (res.status == 200) {
            denominations3G = res.denominations3G; 
            console.log('3gDenominations: ', denominations3G);
            callback(denominations3G)
        } else {
            console.log(res.error)
        }
    }

    ajax('ajax/plans/3g', null, _recv3gDenominations)
}

function getFullTalktimeDenominations(callback)
{
    var _recvFTTDenominations = function(r) {
        console.log(r)
        res = JSON.parse(r)
        if (res.status == 200) {
            denominationsFTT = res.denominationsFullTalktime; 
            console.log('FTTDenominations: ', denominationsFTT);
            callback(denominationsFTT)
        } else {
            console.log(res.error)
        }
    }

    ajax('ajax/plans/fullTalktime', null, _recvFTTDenominations)
}
