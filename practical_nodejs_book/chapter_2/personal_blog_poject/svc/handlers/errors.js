class ExpressError extends Error {
  constructor(message, status) {
    super(message);
    Error.captureStackTrace(this, this.constructor);
    this.name = this.constructor;
    this.statusCode = status || 500;
  }
}

class BadRequestError extends ExpressError {
  constructor(message) {
    super(message, 400);
  }
}

class UnauthorizedError extends ExpressError {
  constructor(message) {
    super(message, 401);
  }
}

class ForbiddenError extends ExpressError {
  constructor(message) {
    super(message, 403);
  }
}

class NotFoundError extends ExpressError {
  constructor(message) {
    super(message, 404);
  }
}

module.exports = {
  ExpressError: ExpressError,
  BadRequestError: BadRequestError,
  UnauthorizedError: UnauthorizedError,
  ForbiddenError: ForbiddenError,
  NotFoundError: NotFoundError
};