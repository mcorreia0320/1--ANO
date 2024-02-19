module.exports = (sequelize, DataTypes) =>{
    return sequelize.define('userHome',{
        user_home_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        amount_people: {
            type: DataTypes.INTEGER,
            allowNull: true
        },
        size: {
            type: DataTypes.FLOAT,
            allowNull: true
        },
        recycling: {
            type: DataTypes.BOOLEAN,
            allowNull: true
        },
        total_co2_emissions: {
            type: DataTypes.FLOAT,
            allowNull: true
        }
    });
}