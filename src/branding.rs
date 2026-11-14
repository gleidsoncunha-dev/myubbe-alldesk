pub(crate) fn initialize() {
    use hbb_common::config::APP_NAME;

    let mut name = APP_NAME.write().unwrap();
    if name.as_str() == "RustDesk" {
        *name = "MyUbbeAllDesk".to_owned();
    }
}
