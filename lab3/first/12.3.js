function multiplyNumeric(obj) {
    for(let key in obj) {
        if(typeof obj[key] == num) {
            obj[key] *= 2;
        }
    }
}