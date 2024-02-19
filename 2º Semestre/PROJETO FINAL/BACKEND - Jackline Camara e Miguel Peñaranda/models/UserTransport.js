module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('user_transport',{
        user_transport_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        distance_traveled: {
            type: DataTypes.FLOAT,
            allowNull: true
        },
        CO2_emissions: {
            type: DataTypes.FLOAT,
            allowNull: true
        }
    });
}