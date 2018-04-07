/**
 * 格式化时间
 * 
 * @param {String} str
 * @returns 格式化后的时间
 */
// export const formatDate = (str) => {
//     if (!str) return ''
//     var date = new Date(str)
//     var time = new Date().getTime() - date.getTime() //现在的时间-传入的时间 = 相差的时间（单位 = 毫秒）
//     if (time < 0) {
//         return ''
//     } else if ((time / 1000 < 30)) {
//         return '刚刚'
//     } else if (time / 1000 < 60) {
//         return parseInt((time / 1000)) + '秒前'
//     } else if ((time / 60000) < 60) {
//         return parseInt((time / 60000)) + '分钟前'
//     } else if ((time / 3600000) < 24) {
//         return parseInt(time / 3600000) + '小时前'
//     } else if ((time / 86400000) < 31) {
//         return parseInt(time / 86400000) + '天前'
//     } else if ((time / 2592000000) < 12) {
//         return parseInt(time / 2592000000) + '月前'
//     } else {
//         return parseInt(time / 31536000000) + '年前'
//     }
// }
/**
 * author haoxj
 * on 1505985374000
 */
/**
 * 对日期进行格式化， 
 * @param date 要格式化的日期 
 * @param format 进行格式化的模式字符串
 *     支持的模式字母有： 
 *     y:年, 
 *     M:年中的月份(1-12), 
 *     d:月份中的天(1-31), 
 *     h:小时(0-23), 
 *     m:分(0-59), 
 *     s:秒(0-59), 
 *     S:毫秒(0-999),
 *     q:季度(1-4)
 * @return String
 */

 // 使用方法 |formatDate('yyyy-MM-dd hh:mm')
 export const formatDate = (str, format) => {
    if (!str) return ''
    // console.log(str,fromat)
    var date = new Date(str);

    var map = {
        "M": date.getMonth() + 1, //月份 
        "d": date.getDate(), //日 
        "h": date.getHours(), //小时 
        "m": date.getMinutes(), //分 
        "s": date.getSeconds(), //秒 
        "q": Math.floor((date.getMonth() + 3) / 3), //季度 
        "S": date.getMilliseconds() //毫秒 
    };
    format = format.replace(/([yMdhmsqS])+/g, function (all, t) {
        var v = map[t];
        if (v !== undefined) {
            if (all.length > 1) {
                v = '0' + v;
                v = v.substr(v.length - 2);
            }
            return v;
        }
        else if (t === 'y') {
            return (date.getFullYear() + '').substr(4 - all.length);
        }
        return all;
    });
    return format;
}
 // 使用方法 |currency('￥',2)
export function currency (value, currency, decimals) {
  var digitsRE = /(\d{3})(?=\d)/g
  value = parseFloat(value)
  if (!isFinite(value) || (!value && value !== 0)) return ''
  currency = currency != null ? currency : '$'
  decimals = decimals != null ? decimals : 2
  var stringified = Math.abs(value).toFixed(decimals)
  var _int = decimals
    ? stringified.slice(0, -1 - decimals)
    : stringified
  var i = _int.length % 3
  var head = i > 0
    ? (_int.slice(0, i) + (_int.length > 3 ? ',' : ''))
    : ''
  var _float = decimals
    ? stringified.slice(-1 - decimals)
    : ''
  var sign = value < 0 ? '-' : ''
  return sign + currency + head +
    _int.slice(i).replace(digitsRE, '$1,') +
    _float
}

export function twoNumber(value){
    if (!value) { return ''}
    return value.toFixed(2);
}
