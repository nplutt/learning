class ExpressError extends Error {
  constructor(message, status) {
    super(message);
    Error.captureStackTrace(this, this.constructor);
    this.name = this.constructor;
    this.statusCode = status || 500;
  }
}

module.exports = class BadRequestError extends ExpressError {
  constructor(message) {
    super(message, 400);
  }
};

module.exports = class UnauthorizedError extends ExpressError {
  constructor(message) {
    super(message, 401);
  }
};

module.exports = class ForbiddenError extends ExpressError {
  constructor(message) {
    super(message, 403);
  }
};

module.exports = class NotFoundError extends ExpressError {
  constructor(message) {
    super(message, 404);
  }
};

module.exports = ExpressError;