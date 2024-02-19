module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('electricity_consumption',{
        electricity_consumption_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        monthly_consumption: {
            type: DataTypes.STRING,
            allowNull: true
        },
        co2_emissions: {
            type: DataTypes.FLOAT,
            allowNull: true
        }
    });
}