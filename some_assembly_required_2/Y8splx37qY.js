const name_list = ['copy_char', 'value', '207aLjBod', '1301420SaUSqf', '233ZRpipt', '2224QffgXU', 'check_flag', '408533hsoVYx', 'instance', '278338GVFUrH', 'Correct!', '549933ZVjkwI', 'innerHTML', 'charCodeAt', './aD8SvhyVkb', 'result', '977AzKzwq', 'Incorrect!', 'exports', 'length', 'getElementById', '1jIrMBu', 'input', '615361geljRK'];

const name_selector = function(arg1, arg2) {
    arg1 = arg1 - 195;
    let selected_name = name_list[arg1];
    return selected_name;
};

(function(arg1, arg2) {
    const _name_selector = name_selector;
    while (!![]) {
        try {
            const some_int = -parseInt(_name_selector(0xc8)) * -parseInt(_name_selector(0xc9)) + -parseInt(_name_selector(0xcd)) + parseInt(_name_selector(0xcf)) + parseInt(_name_selector(195)) + -parseInt(_name_selector(0xc6)) * parseInt(_name_selector(0xd4)) + parseInt(_name_selector(0xcb)) + -parseInt(_name_selector(0xd9)) * parseInt(_name_selector(0xc7));
            if (some_int === arg2)
                break;
            else
                arg1['push'](arg1['shift']());
        } catch (_0x4f8a) {
            arg1['push'](arg1['shift']());
        }
    }
}(name_list, 310022));

let exports;

(async () => {
    const _name_selector = name_selector;
    let some_name = await fetch(_name_selector(210)),
        wasm = await WebAssembly['instantiate'](await some_name['arrayBuffer']()),
        wasm_symbol = wasm[_name_selector(204)];
        exports = wasm_symbol[_name_selector(214)];
})();

function onButtonPress() {
    const _name_selector = name_selector;
    let some_doc_comp = document[_name_selector(0xd8)](_name_selector(0xda))[_name_selector(0xc5)];
    for (let i = 0; i < some_doc_comp['length']; i++) {
        exports[_name_selector(196)](some_doc_comp[_name_selector(209)](i), i);
    }
    exports['copy_char'](0, some_doc_comp[_name_selector(0xd7)]),
    exports[_name_selector(0xca)]() == 0x1 ?
        document['getElementById'](_name_selector(0xd3))[_name_selector(0xd0)] = _name_selector(0xce):
        document[_name_selector(0xd8)](_name_selector(0xd3))['innerHTML'] = _name_selector(0xd5);
}
