use axum::{Router, routing::get};
use battery::Manager;

#[tokio::main]
async fn main() {
    let app = Router::new().route("/metrics", get(metrics));

    let listener = tokio::net::TcpListener::bind("0.0.0.0:9111").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

async fn metrics() -> String {
    format!("battery_level {}", get_battery())
}

fn get_battery() -> f32 {
    let manager = Manager::new().unwrap();
    manager
        .batteries()
        .unwrap()
        .next()
        .unwrap()
        .unwrap()
        .state_of_charge()
        .value
}

#[test]
fn test() {
    dbg!(get_battery());
}
