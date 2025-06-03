db = db.getSiblingDB("moores_law_db");

db.createUser({
  user: "ml_user",
  pwd: "securepassword",
  roles: [
    { role: "dbOwner", db: "moores_law_db" },
    { role: "readWrite", db: "moores_law_db_test" }
  ]
})
db = db.getSiblingDB("moores_law_db_test");

db.createUser({
  user: "ml_user_test",
  pwd: "testpassword",
  roles: [
    { role: "readWrite", db: "moores_law_db_test" },
    { role: "read", db: "moores_law_db" }
  ]
});