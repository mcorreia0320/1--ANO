module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('diet',{
        diet_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        diet_type: {
            type: DataTypes.STRING
        }
    });
}