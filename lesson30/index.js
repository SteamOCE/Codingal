var fe = document.forms['obydaform'];

function validateFromByObyda() {
    if (fe['fullname'].value == 'abc') {
        alert("Wrong details submitted, liar");
        return false;
    }

    if (fe['address'].value == 'abc') {
        alert("Wrong details submitted, liar");
        return false;
    }

    if (fe['phonenumber'].value == 'abc') {
        alert("Wrong details submitted, liar");
        return false;
    }

    // continue with writing the code to save the order in database
    return true;
}