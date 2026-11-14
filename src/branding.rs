pub(crate) fn initialize() {
    use hbb_common::config::{APP_NAME, DEFAULT_SETTINGS};

    let mut name = APP_NAME.write().unwrap();
    if name.as_str() == "RustDesk" {
        *name = "MyUbbeAllDesk".to_owned();
    }
    drop(name);

    let mut settings = DEFAULT_SETTINGS.write().unwrap();
    for (key, value) in [
        ("custom-rendezvous-server", SERVER),
        ("relay-server", SERVER),
        ("key", SERVER_KEY),
    ] {
        settings
            .entry(key.to_owned())
            .or_insert_with(|| value.to_owned());
    }
}

pub(crate) const SERVER: &str = "195.182.200.177";
pub(crate) const SERVER_KEY: &str = "H5N5hffKtcU9fT+oW5I47nk2kS0P2ULAQCHsSaqrryw=";

#[cfg(test)]
mod tests {
    #[test]
    fn published_profile_matches_embedded_server() {
        use hbb_common::base64::{engine::general_purpose::STANDARD, Engine as _};

        let profile: crate::custom_server::CustomServer =
            serde_json::from_str(include_str!("../deploy/client-config.json")).unwrap();
        assert_eq!(profile.host, super::SERVER);
        assert_eq!(profile.relay, super::SERVER);
        assert_eq!(profile.key, super::SERVER_KEY);
        assert_eq!(STANDARD.decode(&profile.key).unwrap().len(), 32);
        assert!(profile.api.is_empty());
    }
}
