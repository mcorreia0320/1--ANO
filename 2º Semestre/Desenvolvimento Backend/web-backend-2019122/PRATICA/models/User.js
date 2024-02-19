module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('users', {
        user_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        name: {
            type: DataTypes.STRING
        },
        age: {
            type: DataTypes.INTEGER
        },
        genre: {
            type: DataTypes.STRING
        }
    })
}