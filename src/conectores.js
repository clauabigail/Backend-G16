import { PrismaClient } from '@prisma/client'

// export const conexion1 = new PrismaClient({datasources: 'mysql://usuario:password@host:3306/my_db'})

export const conexion = new PrismaClient()

// A algunos compañeros les salio error
// PrismaClientInitializationError
// Para solucionar el problema de la variable de entorno corrigieron el codigo (para que Prisma lo lea) de la siguiente manera
// export const conexion = new PrismaClient({
//   datasources:{
//        db: {url: process.env.DATABASE_URL2}
//    }
// })