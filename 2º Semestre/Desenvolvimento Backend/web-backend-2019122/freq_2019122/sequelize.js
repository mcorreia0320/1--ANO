const { Sequelize, DataTypes } = require('sequelize');

const StudentsDataModel = require('./models/Students');
const GradesDataModel = require('./models/Grades');
const CoursesDataModel = require('./models/Courses');

const sequelize = new Sequelize(process.env.DB_SCHEMA, process.env.DB_USER, process.env.DB_PASS, {
    dialect: 'mysql',
    host: process.env.DB_HOST
});

const Student = StudentsDataModel(sequelize, DataTypes);
const Grade = GradesDataModel(sequelize, DataTypes);
const Course = CoursesDataModel(sequelize, DataTypes);

Student.hasMany(Grade);
Grade.belongsTo(Student, {foreignKey: 'student_id'});

Course.hasMany(Grade);
Grade.belongsTo(Course, {foreignKey: 'course_id'});

sequelize.authenticate()
    .then(()=> {
        console.log("Connection has been established")
    })
    .catch(err => {
        console.error("Unable to connect",err);
    });

sequelize.sync({ force: false })
     .then(()=>{
         console.log('Database & tables created!');
     });

// Student.bulkCreate([
//     {first_name: 'Miguel', last_name: 'Correia', email: 'miguel@gmail.com'},
//     {first_name: 'Saul', last_name: 'Pinto', email: 'saul@gmail.com'},
//     {first_name: 'Jacky', last_name: 'Camara', email: 'jacky@gmail.com'}
// ])

// Course.bulkCreate([
//     {course_name: 'Programação', instructor: 'David Jardim'},
//     {course_name: 'Marketing', instructor: 'Marco Olim'},
//     {course_name: 'Matematica', instructor: 'Antonio Pereira'}
// ])

// Grade.bulkCreate([
//     {student_id: 1, course_id: 1, grade: 20},
//     {student_id: 2, course_id: 2, grade: 19},
//     {student_id: 3, course_id: 3, grade: 18}
// ])

module.exports ={
    Student, Grade, Course
}
